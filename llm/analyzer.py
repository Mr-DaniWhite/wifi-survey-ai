from pathlib import Path

from llm.client import OllamaClient
from llm.prompt import build_prompt


def generate_report(snapshot: dict) -> str:
    """
    Genera un informe utilizando Ollama.
    """

    prompt = build_prompt(snapshot)

    # Guardar el prompt para depuración
    Path("debug_prompt.txt").write_text(
        prompt,
        encoding="utf-8",
    )

    client = OllamaClient()

    return client.generate(prompt)