import subprocess


def get_ping(host: str = "1.1.1.1") -> str:
    result = subprocess.run(
        ["ping", "-n", "4", host],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )

    return result.stdout