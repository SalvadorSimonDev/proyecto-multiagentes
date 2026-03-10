from langchain_core.messages import HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from core.state import AgentState

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)

def security_agent(state: AgentState):
    """
    Analiza código en busca de vulnerabilidades, secretos expuestos 
    y dependencias dudosas.
    """
    system_message = SystemMessage(
        content=(
            "Eres un DevSecOps Engineer altamente cualificado. "
            "Tu único propósito es buscar vulnerabilidades de seguridad en el código, "
            "identificar secretos hardcodeados (como API keys o contraseñas), y "
            "advertir sobre el uso de funciones inseguras."
        )
    )
    
    messages = [system_message] + list(state["messages"])
    
    response = llm.invoke(messages)
    
    return {"messages": [response], "current_agent": "security"}
