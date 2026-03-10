from typing import TypedDict, Annotated, Sequence
import operator
from langchain_core.messages import BaseMessage


class AgentState(TypedDict):
    """
    Estado global del sistema.
    Representa la memoria de la sesión que pasa por los diferentes agentes.
    """
    messages: Annotated[Sequence[BaseMessage], operator.add]
    current_agent: str
    context: dict
