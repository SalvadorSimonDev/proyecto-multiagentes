# 🗺️ Roadmap del Proyecto Multiagentes

> Estado del proyecto: **En planificación**  
> Última actualización: 2026-03-09

---

## 🛠️ Fase 1: Infraestructura y Orquestación (El "Cerebro")

> **Objetivo:** Pasar de prompts aislados a flujos de trabajo con estado.

### Framework de Orquestación
- [ ] Implementar **LangGraph** como framework de orquestación principal (alternativa rápida: CrewAI)
  - [ ] Definir el **Grafo de Estado** global que persistirá la memoria de la sesión del desarrollador

### GraphRAG (Memoria Semántica)
- [ ] Indexar la **estructura del código**, no solo texto plano
  - [ ] Usar **tree-sitter** para parsear el AST (Abstract Syntax Tree)
  - [ ] Subir el grafo a una **DB de grafos (Neo4j)** conectada a una **Vector DB (Pinecone / Weaviate)**

### Observabilidad y Tracing
- [ ] Integrar **LangSmith** o **Arize Phoenix** para trazabilidad
  - [ ] Configurar alertas para "alucinaciones" o bucles infinitos de agentes en el CI/CD

---

## 🤖 Fase 2: Definición de Agentes Especializados

> **Objetivo:** Cada agente debe tener una "System Instruction" que actúe como su contrato laboral.

### Agente de Estilo y Clean Code
- [ ] Definir misión: validar que el código sigue las guías internas (naming, arquitectura hexagonal, etc.)
  - [ ] Definir input: **Diff del Pull Request**
  - [ ] Escribir la System Instruction del agente

### Agente de Seguridad y Vulnerabilidades
- [ ] Definir misión: escaneo proactivo de secretos en commits y análisis de dependencias (SBOM)
  - [ ] Conectar el agente con APIs de **Snyk** o **OSV.dev**
  - [ ] Escribir la System Instruction del agente

### Agente de Testing Automático
- [ ] Definir misión: por cada nueva función, generar el Unit Test y el Mock de datos correspondiente
  - [ ] Ejecutar los tests en un entorno aislado (**Docker**) y reportar resultado
  - [ ] Escribir la System Instruction del agente

### Agente de Documentación (Doc-as-Code)
- [ ] Definir misión: mantener el README y la documentación de API (Swagger / OpenAPI) sincronizada con los cambios de código
  - [ ] Escribir la System Instruction del agente

---

## ⚙️ Fase 3: Integración en el SDLC (Flujo de Trabajo)

> **Objetivo:** Donde la IA se encuentra con el proceso real de la empresa.

### PromptOps (Versionado de Prompts)
- [ ] Tratar los prompts **como código** — nada de prompts hardcodeados
  - [ ] Crear un repositorio central de prompts con versionado **SemVer**
  - [ ] Asegurar que todos los servicios consuman la misma "lógica de negocio IA"

### Human-in-the-Loop (HITL)
- [ ] Crear un **Checkpoint** en el grafo de flujo
  - [ ] Integrar con **Slack** o **GitHub Actions** para que el agente solicite aprobación antes de hacer commit
  - [ ] Definir el mensaje estándar del agente: *"He refactorizado esto, ¿puedo hacer el commit?"*

### Evaluación de Salida (LLM-as-a-Judge)
- [ ] Configurar un modelo juez superior (ej. **GPT-4o** o **Claude 3.5 Sonnet**) que evalúe el trabajo del modelo operativo (ej. **Llama 3** o **Gemini Flash**) antes de entregarlo al humano

---

## 🛡️ Fase 4: Gobierno y Calidad (Buenas Prácticas)

> **Objetivo:** Para que el sistema sea profesional y no un juguete.

### Sandboxing de Ejecución
- [ ] Política: los agentes **NUNCA** ejecutan código en el host
  - [ ] Configurar **E2B** o contenedores efímeros para que el agente pruebe su código en aislamiento total

### Medición de ROI de IA
- [ ] Implementar métricas de **Lead Time** (tiempo desde el primer commit hasta el merge)
  - [ ] Comparar flujos con y sin agentes para calcular el impacto real

### Cache de Inferencia
- [ ] Implementar **GPTCache** para evitar pagar (y esperar) por consultas idénticas de los agentes sobre el mismo codebase

---

## 📊 Resumen de Progreso

| Fase | Descripción | Estado |
|------|-------------|--------|
| Fase 1 | Infraestructura y Orquestación | 🔴 Pendiente |
| Fase 2 | Agentes Especializados | 🔴 Pendiente |
| Fase 3 | Integración en el SDLC | 🔴 Pendiente |
| Fase 4 | Gobierno y Calidad | 🔴 Pendiente |
