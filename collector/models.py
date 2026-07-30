from pydantic import BaseModel


class WifiSnapshot(BaseModel):
    ssid: str
    bssid: str | None = None
    signal: int
    rssi: int
    band: str
    channel: int
    radio_type: str
    authentication: str
    cipher: str
    receive_rate: float
    transmit_rate: float