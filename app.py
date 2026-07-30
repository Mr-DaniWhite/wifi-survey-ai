from datetime import datetime
from pathlib import Path
import json

from collector.windows import get_interfaces, get_networks
from collector.ping import get_ping
from collector.speedtest import get_speedtest

from collector.parser import (
    parse_interface,
    parse_networks,
    parse_ping,
    parse_speedtest,
)

from analyzer.scoring import (
    analyze_wifi,
    analyze_environment,
)

from llm.analyzer import generate_report


def main():

    print("📶 Capturando información WiFi...")
    wifi = parse_interface(get_interfaces())

    print("📡 Escaneando redes cercanas...")
    networks = parse_networks(get_networks())

    print("🏓 Ejecutando ping...")
    ping = parse_ping(get_ping())

    print("🚀 Ejecutando Speedtest...")
    speedtest = parse_speedtest(get_speedtest())

    print("📊 Analizando resultados...")
    wifi_analysis = analyze_wifi(wifi)
    environment = analyze_environment(networks)

    snapshot = {
        "timestamp": datetime.now().isoformat(),
        "wifi": wifi.model_dump(),
        "wifi_analysis": wifi_analysis,
        "networks": [network.model_dump() for network in networks],
        "environment": environment,
        "ping": ping.model_dump(),
        "speedtest": speedtest.model_dump(),
    }

    # -----------------------------
    # Guardar snapshot JSON
    # -----------------------------

    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)

    snapshot_file = data_dir / "wifi_snapshot.json"

    with snapshot_file.open(
        "w",
        encoding="utf-8",
    ) as f:
        json.dump(
            snapshot,
            f,
            indent=4,
            ensure_ascii=False,
        )

    print("🤖 Generando informe con Ollama...")

    report = generate_report(snapshot)

    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    report_file = reports_dir / "report.md"

    report_file.write_text(
        report,
        encoding="utf-8",
    )

    print()
    print("========================================")
    print("           WiFi Survey AI")
    print("========================================")
    print(f"SSID                 : {wifi.ssid}")
    print(f"Redes detectadas     : {len(networks)}")
    print(f"RSSI                 : {wifi.rssi} dBm")
    print(f"Canal                : {wifi.channel}")
    print(f"Ping medio           : {ping.average_ms} ms")
    print(f"Descarga             : {speedtest.download_mbps:.2f} Mbps")
    print(f"Subida               : {speedtest.upload_mbps:.2f} Mbps")
    print(f"Servidor Speedtest   : {speedtest.server}")
    print(f"ISP                  : {speedtest.isp}")
    print("----------------------------------------")
    print(f"Snapshot JSON        : {snapshot_file}")
    print(f"Informe IA           : {report_file}")
    print("========================================")


if __name__ == "__main__":
    main()