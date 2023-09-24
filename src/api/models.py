from datetime import datetime
from pydantic import BaseModel


class TemperatureRecord(BaseModel):
    city: str
    temperature: float
    timestamp: str = datetime.utcnow().isoformat(sep=" ")
