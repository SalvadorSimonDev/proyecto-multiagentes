from langchain_google_genai import ChatGoogleGenerativeAI
from core.state import AgentState
from agents.tools import read_file, write_file
from dotenv import load_dotenv

load_dotenv()

# Instanciar el modelo LLM principal (Router) - Cambiado a Google Gemini
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)

from pydantic import BaseModel, Field

class RouteDecision(BaseModel):
    next_node: str = Field(
        description="Si el usuario pide limpieza/arquitectura, devuelve 'clean_code'. "
                    "Si pide seguridad/vulnerabilidades, devuelve 'security'. "
                    "Si pide crear o ejecutar tests, devuelve 'testing'. "
                    "Para cualquier otra consulta general, devuelve 'FIN'."
    )

llm_router = llm.with_structured_output(RouteDecision)

def router_agent(state: AgentState):
    """
    Agente principal que clasifica la intención del usuario y decide el ruteo.
    """
    messages = state["messages"]
    system_message = {
        "role": "system",
        "content": "Eres el enrutador semántico del proyecto multiagentes. Tu única función es leer el mensaje del usuario y decidir qué agente especializado debe atenderlo."
    }
    
    llm_messages = [system_message] + list(messages)
    decision = llm_router.invoke(llm_messages)
    
    # Registramos la decisión en el estado para que el grafo sepa a dónde ir
    return {"current_agent": decision.next_node}
