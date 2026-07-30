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

class WifiNetwork(BaseModel):
    ssid: str
    bssid: str
    signal: int
    radio_type: str
    band: str
    channel: int
    connected_stations: int | None = None
    channel_utilization: int | None = None

class PingResult(BaseModel):
    host: str
    packets_sent: int
    packets_received: int
    packet_loss: int
    minimum_ms: int
    maximum_ms: int
    average_ms: int

