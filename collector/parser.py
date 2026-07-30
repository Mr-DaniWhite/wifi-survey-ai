import re

from collector.models import WifiSnapshot


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