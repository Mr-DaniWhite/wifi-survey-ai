import requests

from llm.config import (
    OLLAMA_URL,
    OLLAMA_MODEL,
    OLLAMA_TIMEOUT,
)


class OllamaClient:

    def generate(self, prompt: str) -> str:

        response = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={
                "model": OLLAMA_MODEL,
                "prompt": "Responde únicamente con la palabra OK.",
                "stream": False,
            },
            timeout=60,
        )

        response.raise_for_status()

        return response.json()["response"]