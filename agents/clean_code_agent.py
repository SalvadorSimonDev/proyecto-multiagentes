from langchain_core.messages import HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from core.state import AgentState

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)

def clean_code_agent(state: AgentState):
    """
    Analiza código para asegurar que sigue las convenciones de Clean Code 
    y Arquitectura Limpia.
    """
    system_message = SystemMessage(
        content=(
            "Eres un Senior Staff Engineer experto en Clean Code, principios SOLID "
            "y Arquitectura Hexagonal. Tu trabajo es revisar el código proporcionado "
            "y sugerir mejoras de legibilidad, arquitectura y tipado estricto."
        )
    )
    
    # Preparamos los mensajes: El system prompt más la historia del estado
    messages = [system_message] + list(state["messages"])
    
    response = llm.invoke(messages)
    
    return {"messages": [response], "current_agent": "clean_code"}
