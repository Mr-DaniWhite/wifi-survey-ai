import shutil
import subprocess


def get_speedtest() -> str:
    """
    Ejecuta Ookla Speedtest CLI y devuelve el JSON como texto.
    """

    exe = shutil.which("speedtest")

    if exe is None:
        raise RuntimeError("No se encontró speedtest.exe en el PATH.")

    print(f"Usando Speedtest: {exe}")

    result = subprocess.run(
        [
            exe,
            "--accept-license",
            "--accept-gdpr",
            "--format=json",
        ],
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=True,
    )

    return result.stdout