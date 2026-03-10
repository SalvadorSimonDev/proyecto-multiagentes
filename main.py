import os
from langchain_core.messages import HumanMessage
from core.orchestrator import app

def main():
    # Asegurarnos de que el usuario haya configurado su API key
    if not os.getenv("OPENAI_API_KEY") and not os.getenv("ANTHROPIC_API_KEY"):
        print("⚠️ Advertencia: No se encontraron API keys de OpenAI o Anthropic en las variables de entorno.")
        print("Por favor, crea un archivo .env en la raíz del proyecto y añade tu API key.")
        return

    print("🤖 Iniciando Orquestador Multiagentes...")
    print("Escribe 'salir' para terminar la ejecución.\n")
    
    # ID de configuración para la persistencia de memoria (Checkpointer)
    config = {"configurable": {"thread_id": "sesion_desarrollo_1"}}
    
    while True:
        user_input = input("Usuario: ")
        if user_input.lower() in ['salir', 'exit', 'quit']:
            break
            
        # Preparar el input para el grafo
        initial_state = {
            "messages": [HumanMessage(content=user_input)]
        }
        
        # Ejecutar el grafo
        print("\nAgent (pensando...)\n")
        try:
            # invoke() corre el grafo entero hasta el final
            result = app.invoke(initial_state, config=config)
            
            # Imprimir el último mensaje generado por el sistema
            last_message = result["messages"][-1]
            print(f"Sistema ({result['current_agent']}): {last_message.content}\n")
            
        except Exception as e:
            print(f"\n❌ Se produjo un error durante la ejecución: {e}\n")

if __name__ == "__main__":
    main()
