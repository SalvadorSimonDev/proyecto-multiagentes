from langchain_core.messages import SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from core.state import AgentState

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0.7)

def chat_agent(state: AgentState):
    """
    Agente para conversación general y explicaciones sobre el sistema.
    """
    system_message = SystemMessage(
        content=(
            "Eres el asistente virtual del Proyecto Multiagentes. "
            "Tu objetivo es ser amable, saludar al usuario y explicar qué puedes hacer "
            "(revisión de clean code, análisis de seguridad y generación de tests). "
            "Responde de forma concisa y profesional en español."
        )
    )
    
    messages = [system_message] + list(state["messages"])
    response = llm.invoke(messages)
    
    return {"messages": [response], "current_agent": "chat"}
