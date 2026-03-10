from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from core.state import AgentState
from agents.router import router_agent

# Configurar el Checkpointer en memoria (después migraremos a SQLite/Postgres)
memory = MemorySaver()

# Inicializar el grafo con el esquema de estado
workflow = StateGraph(AgentState)

# Añadir los nodos (agentes)
workflow.add_node("router", router_agent)

# Configurar el flujo: Empezar en el router y por ahora, terminar.
workflow.set_entry_point("router")
workflow.add_edge("router", END)

# Compilar el grafo conectando la memoria
app = workflow.compile(checkpointer=memory)
