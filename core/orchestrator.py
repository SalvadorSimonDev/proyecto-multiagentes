from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.sqlite import SqliteSaver
import sqlite3
from core.state import AgentState
from agents.router import router_agent
from agents.chat_agent import chat_agent
from agents.clean_code_agent import clean_code_agent
from agents.security_agent import security_agent
from agents.testing_agent import testing_agent

# Configurar el Checkpointer con SQLite para persistencia real
# Usamos un archivo local 'checkpoints.db'
conn = sqlite3.connect("checkpoints.db", check_same_thread=False)
memory = SqliteSaver(conn)

# Inicializar el grafo con el esquema de estado
workflow = StateGraph(AgentState)

# Añadir los nodos (agentes)
workflow.add_node("router", router_agent)
workflow.add_node("chat", chat_agent)
workflow.add_node("clean_code", clean_code_agent)
workflow.add_node("security", security_agent)
workflow.add_node("testing", testing_agent)

def router_condition(state: AgentState) -> str:
    """Función de enrutamiento que lee la decisión del router_agent."""
    return state.get("current_agent", "END")

# Configurar el flujo
workflow.set_entry_point("router")

workflow.add_conditional_edges(
    "router",
    router_condition,
    {
        "chat": "chat",
        "clean_code": "clean_code",
        "security": "security",
        "testing": "testing",
        "END": END
    }
)

# Tras ejecutar un especialista, terminamos el flujo
workflow.add_edge("chat", END)
workflow.add_edge("clean_code", END)
workflow.add_edge("security", END)
workflow.add_edge("testing", END)

# Compilar el grafo conectando la memoria
app = workflow.compile(checkpointer=memory)
