"""
WiFi Survey AI - Scoring Engine

Este módulo contiene las reglas para puntuar la calidad de una conexión WiFi.
No obtiene datos del sistema ni genera informes; únicamente analiza los
modelos recibidos desde el collector.
"""

from collector.models import WifiSnapshot


def score_signal(rssi: int) -> tuple[int, str]:
    """
    Calcula la puntuación de la intensidad de señal (RSSI).
    """

    if rssi >= -50:
        return 100, "Excelente"

    if rssi >= -60:
        return 90, "Muy buena"

    if rssi >= -67:
        return 80, "Buena"

    if rssi >= -70:
        return 65, "Aceptable"

    if rssi >= -80:
        return 40, "Débil"

    return 10, "Muy débil"


def score_band(band: str) -> tuple[int, str]:
    """
    Puntúa la banda utilizada.
    """

    band = band.lower()

    if "6" in band:
        return 100, "Wi-Fi 6E / 6 GHz"

    if "5" in band:
        return 95, "5 GHz"

    return 70, "2.4 GHz"


def analyze_wifi(wifi: WifiSnapshot) -> dict:
    """
    Analiza la calidad de una conexión WiFi.
    """

    signal_score, signal_status = score_signal(wifi.rssi)

    band_score, band_status = score_band(wifi.band)

    overall = round((signal_score + band_score) / 2)

    return {
        "overall": overall,
        "signal": {
            "score": signal_score,
            "status": signal_status,
        },
        "band": {
            "score": band_score,
            "status": band_status,
        },
    }
from collections import Counter
from collector.models import WifiNetwork


def networks_per_channel(networks: list[WifiNetwork]) -> dict[int, int]:
    """
    Devuelve el número de redes detectadas por canal.
    """

    counter = Counter()

    for network in networks:
        counter[network.channel] += 1

    return dict(sorted(counter.items()))


def best_channel(networks: list[WifiNetwork]) -> int:
    """
    Devuelve el canal menos congestionado.
    """

    channels = networks_per_channel(networks)

    if not channels:
        return 0

    return min(channels, key=channels.get)


def analyze_environment(networks: list[WifiNetwork]) -> dict:

    channels = networks_per_channel(networks)

    return {
        "visible_networks": len(networks),
        "channels": channels,
        "recommended_channel": best_channel(networks),
    }