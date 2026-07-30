# WiFi Survey AI

WiFi Survey AI es una herramienta de diagnóstico de redes WiFi para Windows que recopila información de la conexión inalámbrica, analiza el rendimiento de la red y genera un informe inteligente utilizando un modelo LLM ejecutado localmente con Ollama.

## Características

- 📶 Captura información de la interfaz WiFi (`netsh`)
- 📡 Escanea redes cercanas
- 🏓 Ejecuta pruebas de latencia (Ping)
- 🚀 Ejecuta Speedtest CLI (Ookla)
- 📊 Calcula métricas básicas de calidad
- 🤖 Genera un informe técnico mediante Gemma 3 ejecutándose en Ollama
- 💾 Guarda un snapshot JSON con todos los datos recopilados

## Arquitectura

```
collector/
    windows.py
    parser.py
    ping.py
    speedtest.py

analyzer/
    scoring.py

llm/
    config.py
    client.py
    prompt.py
    analyzer.py

data/
reports/

app.py
```

## Requisitos

- Windows 11
- Python 3.13+
- uv
- Ollama
- Gemma 3
- Ookla Speedtest CLI

## Instalación

```bash
git clone https://github.com/Mr-DaniWhite/wifi-survey-ai.git

cd wifi-survey-ai

uv sync
```

## Configuración

Crear un archivo `.env`

```text
OLLAMA_URL=http://localhost:11434
OLLAMA_MODEL=gemma3:4b
OLLAMA_TIMEOUT=300
```

## Ejecución

```bash
uv run app.py
```

## Salida

Se generan automáticamente:

```
data/
    wifi_snapshot.json

reports/
    report.md
```

## Roadmap

- [x] Captura de datos WiFi
- [x] Ping
- [x] Speedtest
- [x] Integración con Ollama
- [x] Informe Markdown

Próximamente:

- [ ] Históricos de ejecuciones
- [ ] Informe HTML
- [ ] Dashboard web
- [ ] Agente de diagnóstico WiFi
- [ ] Comparación entre snapshots

## Licencia

MIT