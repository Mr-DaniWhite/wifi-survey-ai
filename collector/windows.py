import subprocess


def run_command(command: list[str]) -> str:
    """
    Ejecuta un comando de Windows y devuelve la salida.
    """

    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="ignore",
        shell=False,
    )

    if result.returncode != 0:
        raise RuntimeError(result.stderr)

    return result.stdout


def get_interfaces() -> str:
    return run_command(["netsh", "wlan", "show", "interfaces"])


def get_networks() -> str:
    return run_command(["netsh", "wlan", "show", "networks", "mode=bssid"])