# 🤖 Proyecto Multiagentes

Sistema de orquestación de Agentes Especializados de IA usando **LangGraph** y **LangChain**, diseñado para interactuar de manera autónoma con el código y asistir en el SDLC (Ciclo de Vida del Desarrollo de Software).

## 🚀 Requisitos Previos

- **Python 3.9** o superior.
- Claves de API necesarias:
  - `OPENAI_API_KEY` (Obligatorio para que los agentes puedan procesar información).
  - `ANTHROPIC_API_KEY` (Alternativa si decides cambiar el modelo LLM en el código).
  - `E2B_API_KEY` (Recomendado: Permite al Agente de Testing levantar entornos Sandbox aislados para probar el código sin riesgos).

## 🛠️ Instalación y Configuración

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/SalvadorSimonDev/proyecto-multiagentes.git
   cd proyecto-multiagentes
   ```

2. **Crear y activar un entorno virtual**
   ```bash
   python -m venv .venv
   
   # En Windows:
   .\.venv\Scripts\activate
   # En macOS/Linux:
   source .venv/bin/activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar el entorno**
   Copia el archivo de ejemplo de variables de entorno y complétalo con tus datos:
   ```bash
   # Copia el archivo para crear el tuyo local
   cp .env.example .env
   ```
   Abre el nuevo archivo `.env` en tu editor y pega tus API keys reales.

## 🧠 Estructura Actual (Fase 2 Completada)

El sistema cuenta con un Router semántico que redirige tu petición al especialista adecuado:

* `/core/`: Contiene el Orquestador `StateGraph` de LangGraph y la Memoria de corto plazo.
* `/agents/`: 
  * `router.py`: Cerebro principal que lee la petición y decide a qué agente enviarla.
  * `clean_code_agent.py`: Analiza tu código basándose en principios SOLID y arquitectura limpia.
  * `security_agent.py`: Detecta secretos hardcodeados y problemas de seguridad (DevSecOps).
  * `testing_agent.py`: Emplea QA Automation creando pruebas `pytest` y validándolas en un Sandbox efímero usando E2B.

## 💻 ¿Cómo ejecutarlo?

Asegúrate de tener el entorno virtual activado (`.venv` en verde en tu consola) y ejecuta:

```bash
python main.py
```

Esto abrirá un CLI interactivo:
1. Pídele al router lo que necesitas (ej. *"Haz una revisión de clean code en este archivo"* o *"Crea tests unitarios para Auth"*).
2. El sistema pensará, enrutará la petición al agente correcto, ejecutará el código necesario, y te devolverá el resultado por la misma terminal.
3. Escribe `salir` cuando quieras detener la ejecución.
