"""Input and output schemas for models"""

from ninja import Schema


class SensorIn(Schema):
    """Output schema for sensor"""

    dirt: str
    rain: str
    air: str
    sun: str
    pressure: str
    temperature: str
