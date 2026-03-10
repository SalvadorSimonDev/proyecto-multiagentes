from langchain_core.messages import HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from core.state import AgentState
from agents.tools import read_file, write_file
from dotenv import load_dotenv

load_dotenv()

# Instanciar el modelo LLM principal (Router)
# Se pueden usar varios modelos dependiendo del rol (ej: Claude para código, OpenAI para routing rápido)
llm = ChatOpenAI(model="gpt-4o", temperature=0)

# Vincular las herramientas al LLM
tools = [read_file, write_file]
llm_with_tools = llm.bind_tools(tools)

def router_agent(state: AgentState):
    """
    Agente principal que decide el flujo inicial y usa herramientas.
    """
    messages = state["messages"]
    system_message = {
        "role": "system",
        "content": "Eres el Orquestador principal del proyecto multiagentes. Tu objetivo es entender el pedido del usuario y usar tus herramientas para analizar el repositorio."
    }
    
    # Preparar mensajes para el LLM
    llm_messages = [system_message] + list(messages)
    
    # Invocar al modelo
    response = llm_with_tools.invoke(llm_messages)
    
    # Devolver el estado actualizado
    return {"messages": [response], "current_agent": "router"}
