import os
from langchain_core.tools import tool

@tool
def read_file(file_path: str) -> str:
    """Lee el contenido de un archivo dado su path absoluto."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"Error al leer el archivo: {str(e)}"

@tool
def write_file(file_path: str, content: str) -> str:
    """Escribe o sobrescribe un archivo con el contenido proporcionado."""
    try:
        # Crear directorios si no existen
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return f"Archivo {file_path} escrito exitosamente."
    except Exception as e:
        return f"Error al escribir el archivo: {str(e)}"
