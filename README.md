# WiFi Survey AI

> AI-powered WiFi diagnostics for Windows using Ollama and Gemma 3.

WiFi Survey AI is a Python application that collects wireless network information from Windows, performs connectivity tests, and generates an AI-powered technical report using a locally running Large Language Model (LLM) through Ollama.

---

## Features

- 📶 Collects WiFi interface information (`netsh`)
- 📡 Scans nearby wireless networks
- 🏓 Measures latency using Ping
- 🚀 Runs Ookla Speedtest CLI
- 📊 Performs basic WiFi quality analysis
- 🤖 Generates an AI-powered report using Gemma 3 via Ollama
- 💾 Exports a complete JSON snapshot
- 📄 Produces a Markdown technical report

---

## Project Structure

```text
wifi-survey-ai/
│
├── analyzer/
│   └── scoring.py
│
├── collector/
│   ├── models.py
│   ├── parser.py
│   ├── ping.py
│   ├── speedtest.py
│   └── windows.py
│
├── llm/
│   ├── analyzer.py
│   ├── client.py
│   ├── config.py
│   └── prompt.py
│
├── data/
├── reports/
│
├── app.py
├── pyproject.toml
└── README.md
```

---

## Requirements

- Windows 11
- Python 3.13+
- uv
- Ollama
- Gemma 3
- Ookla Speedtest CLI

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Mr-DaniWhite/wifi-survey-ai.git

cd wifi-survey-ai
```

Install dependencies:

```bash
uv sync
```

---

## Configuration

Create a `.env` file in the project root:

```text
OLLAMA_URL=http://localhost:11434
OLLAMA_MODEL=gemma3:4b
OLLAMA_TIMEOUT=300
```

---

## Usage

Run the application:

```bash
uv run app.py
```

---

## Output

The application automatically generates:

```text
data/
    wifi_snapshot.json

reports/
    report.md
```

---

## Technologies

- Python 3.13
- uv
- Ollama
- Gemma 3
- Windows netsh
- Ookla Speedtest CLI

---

## Roadmap

### Version 0.1

- ✅ WiFi information collection
- ✅ Nearby network discovery
- ✅ Ping measurements
- ✅ Speedtest integration
- ✅ JSON snapshot generation
- ✅ AI report generation using Ollama

### Planned Features

- Historical measurements
- HTML reports
- Interactive dashboard
- AI diagnostic agent
- Snapshot comparison
- Multi-language reports
- PDF export

---

## License

MIT License

---

## Author

Daniel Blanco

GitHub: https://github.com/Mr-DaniWhite