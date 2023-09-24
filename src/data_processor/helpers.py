import logging
import requests
from datetime import datetime

from src.config import Config
from src.data_processor.model import OpenWeatherResponse
from src.db.connection import DBConnectionContext
from src.api.models import TemperatureRecord

logger = logging.getLogger(__name__)

PATH = f"https://api.openweathermap.org/data/2.5/weather?q={Config.CITY}&units={Config.UNITS}&appid={Config.WEATHER_API_KEY}"


def get_data() -> OpenWeatherResponse | None:
    response = requests.get(PATH)

    if response.status_code != 200:
        logger.error(f"Failed to get data for {Config.CITY} at {datetime.utcnow()} UTC")
        return None

    try:
        data = OpenWeatherResponse(**response.json())
    except Exception as e:
        logger.error(
            f"Failed to parse data for {Config.CITY} at {datetime.utcnow()} UTC\n"
            f"Error: {repr(e)}"
        )
        return None

    return data


def insert_data(data):
    with DBConnectionContext() as db:
        data = dict(TemperatureRecord(city=Config.CITY, temperature=data.main.temp))
        db.execute(
            f"INSERT INTO temperature({','.join(data.keys())}) VALUES(?, ?, ?)",
            tuple(data.values()),
        )
        db.connection.commit()
