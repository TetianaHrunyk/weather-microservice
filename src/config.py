from logging.config import dictConfig

logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {"format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"}
    },
    "handlers": {
        "default": {
            "level": "INFO",
            "formatter": "standard",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        }
    },
    "root": {"handlers": ["default"], "level": "INFO", "propagate": False},
}

dictConfig(logging_config)


class Config:
    CITY = "Kyiv"
    APPLICATION_X_TOKEN = "asjdh98as7agejh325l4359ta1ysfdof"

    WEATHER_API_KEY = ""
    UNITS = "metric"

    DATABASE_NAME = "database.db"
    TABLE_NAME = "temperature"
