---
description: Sincroniza el ROADMAP.md local con Issues de GitHub
---

# 🚀 Sincronizador de Roadmap a GitHub Issues

Este flujo de trabajo (workflow) es mi guía automatizada para leer el `ROADMAP.md` y convertir cada tarea pendiente en un Issue formal dentro de un repositorio de GitHub. 

## 📋 Pre-requisitos
- Tener instalada la CLI de GitHub (`gh`) en el sistema Windows del usuario.
- Haber iniciado sesión en la CLI con `gh auth login`.
- El repositorio de GitHub debe estar inicializado.

## 🛠️ Pasos de Ejecución (Para la IA)

Cuando el usuario invoque este flujo (ej. "sincroniza el roadmap en github"), ejecutaré exactamente esto:

1. **Verificación de CLI:**
   Comprobaré si `gh` está instalado y autenticado correctamente.
   ```powershell
   gh auth status
   ```

2. **Creación de Etiquetas (Labels):**
   Crearé las etiquetas de las 4 fases de nuestro proyecto para que el tablero se vea profesional.
   ```powershell
   gh label create "Fase 1: Infraestructura" --color "0e8a16" --force
   gh label create "Fase 2: Agentes" --color "1d76db" --force
   gh label create "Fase 3: SDLC" --color "b60205" --force
   gh label create "Fase 4: Gobierno" --color "d93f0b" --force
   ```

3. **Parseo y Creación de Issues:**
   Leeré el archivo `ROADMAP.md`. Por cada tarea (ej. "Selección del Framework de Orquestación"), ejecutaré dinámicamente el siguiente comando, inyectando la descripción y subtareas en el `--body`:
   
   // turbo
   ```powershell
   gh issue create --title "<TITULO_DE_LA_TAREA>" --body "<DESCRIPCION_Y_SUBTAREAS_EN_MARKDOWN>" --label "<FASE_CORRESPONDIENTE>"
   ```
   *Nota: Reemplazaré los placeholders `<...>` con los datos reales del ROADMAP.*

4. **Feedback al Usuario:**
   Una vez completado, devolveré un resumen al usuario con los links a los Issues creados.
