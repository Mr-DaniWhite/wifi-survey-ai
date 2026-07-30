import re

from collector.models import WifiSnapshot, WifiNetwork, PingResult


def value(text: str, field: str) -> str:
    pattern = rf"{re.escape(field)}\s*:\s*(.+)"
    match = re.search(pattern, text)

    if not match:
        return ""

    return match.group(1).strip()


def parse_interface(text: str) -> WifiSnapshot:
    return WifiSnapshot(
        ssid=value(text, "SSID"),
        signal=int(value(text, "Signal").replace("%", "")),
        rssi=int(value(text, "Rssi")),
        band=value(text, "Band"),
        channel=int(value(text, "Channel")),
        radio_type=value(text, "Radio type"),
        authentication=value(text, "Authentication"),
        cipher=value(text, "Cipher"),
        receive_rate=float(value(text, "Receive rate (Mbps)")),
        transmit_rate=float(value(text, "Transmit rate (Mbps)")),
    )


def parse_networks(text: str) -> list[WifiNetwork]:
    """
    Parsea la salida de:
        netsh wlan show networks mode=bssid
    """

    networks = []
    current_ssid = ""

    lines = text.splitlines()

    i = 0

    while i < len(lines):

        line = lines[i].strip()

        # Nuevo SSID
        match = re.match(r"SSID\s+\d+\s*:\s*(.+)", line)
        if match:
            current_ssid = match.group(1).strip()
            i += 1
            continue

        # Nuevo BSSID
        match = re.match(r"BSSID\s+\d+\s*:\s*(.+)", line)
        if match:

            bssid = match.group(1).strip()

            signal = 0
            radio_type = ""
            band = ""
            channel = 0
            connected_stations = None
            channel_utilization = None

            i += 1

            while i < len(lines):

                line = lines[i].strip()

                # Empieza otro bloque
                if re.match(r"(SSID|BSSID)\s+\d+", line):
                    break

                if ":" in line:
                    key, value = [x.strip() for x in line.split(":", 1)]

                    if key == "Signal":
                        signal = int(value.replace("%", ""))

                    elif key == "Radio type":
                        radio_type = value

                    elif key == "Band":
                        band = value

                    elif key == "Channel":
                        channel = int(value)

                    elif key == "Connected Stations":
                        connected_stations = int(value)

                    elif key == "Channel Utilization":
                        channel_utilization = int(value.split()[0])

                i += 1

            networks.append(
                WifiNetwork(
                    ssid=current_ssid,
                    bssid=bssid,
                    signal=signal,
                    radio_type=radio_type,
                    band=band,
                    channel=channel,
                    connected_stations=connected_stations,
                    channel_utilization=channel_utilization,
                )
            )

            continue

        i += 1

    return networks


def parse_ping(text: str) -> PingResult:
    """
    Parsea la salida de:
        ping -n 4 1.1.1.1
    """

    host_match = re.search(r"Pinging\s+([\d\.]+)", text)
    host = host_match.group(1) if host_match else ""

    packets = re.search(
        r"Packets:\s+Sent\s*=\s*(\d+),\s*Received\s*=\s*(\d+),\s*Lost\s*=\s*(\d+)",
        text,
    )

    times = re.search(
        r"Minimum\s*=\s*(\d+)ms,\s*Maximum\s*=\s*(\d+)ms,\s*Average\s*=\s*(\d+)ms",
        text,
    )

    if not packets:
        raise ValueError("No se pudieron obtener las estadísticas del ping.")

    if not times:
        raise ValueError("No se pudieron obtener los tiempos del ping.")

    sent = int(packets.group(1))
    received = int(packets.group(2))
    lost = int(packets.group(3))

    loss = int((lost / sent) * 100) if sent else 100

    minimum = int(times.group(1))
    maximum = int(times.group(2))
    average = int(times.group(3))

    return PingResult(
        host=host,
        packets_sent=sent,
        packets_received=received,
        packet_loss=loss,
        minimum_ms=minimum,
        maximum_ms=maximum,
        average_ms=average,
    )