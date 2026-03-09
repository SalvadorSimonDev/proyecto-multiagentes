# 🧠 Memoria Central del Proyecto (Contexto del Agente)

> **Propósito:** Este documento sirve como mi memoria a largo plazo. Lo consultaré para recordar el contexto del proyecto, las decisiones de arquitectura, tus preferencias y las lecciones aprendidas sobre el desarrollo de sistemas multiagentes.

## 🎯 Visión General del Proyecto
- **Objetivo:** Construir un sistema multiagentes profesional y escalable para automatizar flujos de desarrollo de software (SDLC).
- **Enfoque:** Pasar de simples prompts a "flujos de trabajo con estado" (Stateful Workflows) donde los agentes interactúan y retienen contexto.

## 🏛️ Decisiones de Arquitectura Tomadas
1. **Orquestador:** LangGraph (preferido por su control granular del estado y capacidad para definir grafos cíclicos, esencial para agentes que iteran).
2. **Memoria:** GraphRAG (Neo4j + Vector DB) escaneando el AST (Abstract Syntax Tree) del código, no solo texto plano.
3. **Observabilidad:** LangSmith o Arize Phoenix para auditar qué hace cada agente y evitar bucles infinitos.
4. **Sandboxing:** E2B o contenedores aislados; los agentes **NUNCA** ejecutan código no confiable directamente en el host.

## 🤖 Mis Reglas de Comportamiento (Como tu IA)
- **Proactividad Extrema:** No debo esperar a que me preguntes todo. Debo proponerte arquitecturas, herramientas modernas y detectar posibles cuellos de botella antes de que ocurran.
- **Sobregiro de Información Útil:** Entregaré detalles de sobra, ejemplos de código y mejores prácticas de la industria sin que me lo pidas.
- **Comunicación:** En español, actuando como un Arquitecto de Software y Tech Lead especializado en IA.

## 💡 Notas Técnicas y Buenas Prácticas de Multiagentes (Proactivas)
*Añadido por la IA para tenerlo siempre presente:*
- **Enrutamiento Semántico (Semantic Routing):** Antes de lanzar un agente complejo, es buena práctica tener un "*Agente Router*" súper rápido (ej. Llama 3 8B) que simplemente clasifique la intención del usuario y dirija el flujo al agente especializado correcto, ahorrando latencia y dinero.
- **Tool Calling vs JSON format:** Siempre preferiremos el uso nativo de *Tool Calling* de los modelos (ej. el de OpenAI/Gemini) en lugar de pedirles que impriman JSONs libres, ya que el Tool Calling garantiza que el output coincida con el esquema esperado.
- **Human-in-the-Loop (HITL) como Estado:** En LangGraph, las interrupciones para pedir permiso al humano se modelan pausando el grafo y guardando el estado en una base de datos (Postgres/SQLite), lo que permite que el sistema se reanude días después sin perder contexto.

---
## 📅 Registro de Sesiones

### Sesión 1: 9 de Marzo de 2026
- **Logros:** 
  - Inicialización del proyecto y repositorio Git (local y remoto).
  - Creación del `ROADMAP.md` con las 4 fases fundamentales (Orquestación, Agentes, SDLC, Gobierno).
  - Creación del `MEMORY.md` para persistir arquitecturas y decisiones.
  - Creación del primer Skill/Workflow (`github_roadmap_sync.md`) para sincronizar el roadmap local con los Issues de GitHub.
  - Ejecución exitosa del workflow: Se crearon 13 Issues y 4 etiquetas semánticas en el repositorio público.
- **Próximos pasos (Para mañana):**
  - Iniciar ejecución de la Fase 1: Setup del entorno base y primer acercamiento al código con **LangGraph** (o framework seleccionado).
  - Definir estructura de carpetas (ej. `/agents`, `/workflows`, `/core`, etc.).

---
*Nota: Este archivo crecerá orgánicamente. Cada vez que tomemos una decisión importante o aprendamos algo nuevo sobre orquestación de LLMs, lo registraré aquí.*
