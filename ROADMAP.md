# 🗺️ Roadmap del Proyecto Multiagentes

> Estado del proyecto: **En planificación**  
> Última actualización: 2026-03-09

---

## 🛠️ Fase 1: Infraestructura y Orquestación (El "Cerebro")

> **Objetivo:** Pasar de prompts aislados a flujos de trabajo con estado.

### Framework de Orquestación
- [x] Implementar **LangGraph** como framework de orquestación principal
  - [x] Definir el **Grafo de Estado** global que persistirá la memoria de la sesión
  - [x] Configurar ruteo semántico entre múltiples agentes especializados

### GraphRAG (Memoria Semántica)
- [ ] Indexar la **estructura del código**, no solo texto plano
  - [ ] Usar **tree-sitter** para parsear el AST (Abstract Syntax Tree)
  - [ ] Subir el grafo a una **DB de grafos (Neo4j)** conectada a una **Vector DB**

### Observabilidad y Tracing
- [x] Seleccionar proveedor de LLM gratuito/estable (Google Gemini 2.5 Flash-Lite)
- [ ] Integrar **LangSmith** o **Arize Phoenix** para trazabilidad

---

## 🤖 Fase 2: Definición de Agentes Especializados

> **Objetivo:** Cada agente debe tener una "System Instruction" que actúe como su contrato laboral.

### Agentes Implementados
- [x] **Agente Router**: Decide qué especialista debe actuar.
- [x] **Agente de Chat**: Saludos e información general del sistema.
- [x] **Agente de Clean Code**: Análisis de calidad y legibilidad.
- [x] **Agente de Seguridad**: Identificación de vulnerabilidades básicas.
- [x] **Agente de Testing**: Generación de tests unitarios (integración con E2B).

### Agentes Pendientes
- [ ] **Agente de Documentación (Doc-as-Code)**: README y Swagger sincronizados.
- [ ] **Agente de Integración GitHub**: Capacidad para leer y escribir PRs de forma autónoma.

---

## ⚙️ Fase 3: Integración en el SDLC (Flujo de Trabajo)

> **Objetivo:** Donde la IA se encuentra con el proceso real de la empresa.

### Persistencia y Jarvis
- [ ] Implementar **PostgresSaver/SQLite** para persistencia de hilos (Thread ID).
- [ ] Integrar con **Telegram Bot API** para acceso móvil y notificaciones.
- [ ] Implementar **Human-in-the-Loop (HITL)** para aprobaciones de código.

### PromptOps
- [ ] Tratar los prompts **como código** — nada de prompts hardcodeados.

---

## 🛡️ Fase 4: Gobierno y Calidad (Buenas Prácticas)

> **Objetivo:** Para que el sistema sea profesional y no un juguete.

### Multimodalidad y Seguridad
- [ ] Implementar Sandboxing total con **E2B**.
- [ ] Soporte para comandos de **Voz (STT)** en Telegram.
- [ ] Análisis de imágenes/diagramas.

---

## 📊 Resumen de Progreso

| Fase | Descripción | Estado |
|------|-------------|--------|
| Fase 1 | Infraestructura y Orquestación | 🟡 En curso |
| Fase 2 | Agentes Especializados | 🟡 En curso |
| Fase 3 | Integración en el SDLC | 🔴 Pendiente |
| Fase 4 | Gobierno y Calidad | 🔴 Pendiente |

