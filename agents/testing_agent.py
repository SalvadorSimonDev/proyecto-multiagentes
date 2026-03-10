import os
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from core.state import AgentState

# Intentamos importar E2B, si no está configurado, avisamos.
try:
    from e2b_code_interpreter import Sandbox
    E2B_AVAILABLE = True
except ImportError:
    E2B_AVAILABLE = False


@tool
def execute_python_code(code: str) -> str:
    """
    Ejecuta código Python arbitrario en un entorno aislado (Sandbox) y 
    devuelve la salida estándar. Útil para verificar si los tests pasan.
    """
    if not E2B_AVAILABLE:
        return "Error: SDK de E2B no instalado. No se puede ejecutar el código."
        
    api_key = os.getenv("E2B_API_KEY")
    if not api_key:
        return "Error: E2B_API_KEY no configurada en las variables de entorno."

    try:
        with Sandbox(api_key=api_key) as sandbox:
            execution = sandbox.run_code(code)
            
            output = ""
            if execution.logs.stdout:
                output += f"STDOUT:\n{''.join(execution.logs.stdout)}\n"
            if execution.logs.stderr:
                output += f"STDERR:\n{''.join(execution.logs.stderr)}\n"
            if execution.error:
                output += f"ERROR:\n{execution.error.name}: {execution.error.value}\n{execution.error.traceback}"
                
            return output if output else "Ejecución exitosa sin output."
            
    except Exception as e:
        return f"Excepción fatal al conectar con sandbox: {str(e)}"


llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0).bind_tools([execute_python_code])

def testing_agent(state: AgentState):
    """
    Genera tests unitarios y los ejecuta en el entorno aislado E2B.
    """
    system_message = SystemMessage(
        content=(
            "Eres un QA Automation Engineer. Tu tarea es generar tests unitarios "
            "en Python (usando la sintaxis base o pytest). Tienes una herramienta "
            "llamada execute_python_code; úsala SIEMPRE para correr los tests que has "
            "generado junto con el código original y comprobar si pasan o fallan."
        )
    )
    
    messages = [system_message] + list(state["messages"])
    
    response = llm.invoke(messages)
    
    return {"messages": [response], "current_agent": "testing"}
