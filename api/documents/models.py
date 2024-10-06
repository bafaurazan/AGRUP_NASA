"""Models structure"""

from django.db import models


class Sensor(models.Model):
    """Sensor model structure"""

    dirt: str = models.TextField()
    rain: str = models.TextField()
    air: str = models.TextField()
    sun: str = models.TextField()
    pressure: str = models.TextField()
    temperature: str = models.TextField()

class Document(models.Model):
    """Document model structure"""

    command: str = models.TextField()
    request_path: str = models.TextField()
    documentation: str = models.TextField(default="No documentation")