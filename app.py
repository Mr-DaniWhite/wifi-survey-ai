from datetime import datetime
from pathlib import Path
import json

from collector.windows import get_interfaces, get_networks
from collector.ping import get_ping

from collector.parser import (
    parse_interface,
    parse_networks,
    parse_ping,
)

from analyzer.scoring import (
    analyze_wifi,
    analyze_environment,
)


def main():
    # Obtener datos del sistema
    wifi = parse_interface(get_interfaces())
    networks = parse_networks(get_networks())
    ping = parse_ping(get_ping())

    # Análisis
    wifi_analysis = analyze_wifi(wifi)
    environment = analyze_environment(networks)

    # Crear snapshot
    snapshot = {
        "timestamp": datetime.now().isoformat(),
        "wifi": wifi.model_dump(),
        "wifi_analysis": wifi_analysis,
        "networks": [network.model_dump() for network in networks],
        "environment": environment,
        "ping": ping.model_dump(),
    }

    # Crear carpeta data si no existe
    output_dir = Path("data")
    output_dir.mkdir(exist_ok=True)

    # Guardar JSON
    output_file = output_dir / "wifi_snapshot.json"

    with output_file.open("w", encoding="utf-8") as f:
        json.dump(snapshot, f, indent=4)

    print("======================================")
    print(" WiFi Survey AI")
    print("======================================")
    print(f"SSID             : {wifi.ssid}")
    print(f"Redes detectadas : {len(networks)}")
    print(f"Ping medio       : {ping.average_ms} ms")
    print(f"Snapshot         : {output_file}")
    print("======================================")


if __name__ == "__main__":
    main()