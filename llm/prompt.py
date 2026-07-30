import json


def build_prompt(snapshot: dict) -> str:
    """
    Construye el prompt que se enviará a Ollama.
    """

    snapshot_json = json.dumps(
        snapshot,
        indent=2,
        ensure_ascii=False,
    )

    return f"""
# Rol

Eres un ingeniero senior especializado en redes WiFi, rendimiento de redes domésticas y diagnóstico de conectividad.

Tu misión es analizar objetivamente la información proporcionada.

Nunca inventes datos.

Si una conclusión no puede deducirse a partir de la información disponible, indícalo explícitamente.

Utiliza un lenguaje técnico pero comprensible para un usuario avanzado.

---

# Criterios de evaluación

Evalúa especialmente:

- Calidad de la señal WiFi
- Banda utilizada
- Canal utilizado
- Velocidad de enlace WiFi
- Nivel RSSI
- Ping
- Jitter
- Velocidad de descarga
- Velocidad de subida
- Posible saturación del canal
- Número de redes detectadas
- Número de clientes conectados
- Utilización del canal
- Posibles problemas de cobertura
- Posibles problemas del ISP
- Posibles problemas de configuración

---

# Datos capturados

{snapshot_json}

---

# Devuelve SIEMPRE el resultado en Markdown usando exactamente esta estructura

# Resumen ejecutivo

Un resumen de unas pocas líneas.

# Estado de la red WiFi

Explica la calidad de la conexión inalámbrica.

# Rendimiento de Internet

Analiza ping, descarga y subida.

# Posibles problemas detectados

Lista únicamente los problemas encontrados.

# Recomendaciones

Enumera las acciones recomendadas por prioridad.

# Puntuación final

Asigna una puntuación global entre 0 y 100.

Justifica brevemente la puntuación.
"""