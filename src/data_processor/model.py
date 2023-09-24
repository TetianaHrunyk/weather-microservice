from pydantic import BaseModel


class OpenWeatherResponseMain(BaseModel):
    """
    Field `main` from the OpenWeatherResponse
    """

    temp: float


class OpenWeatherResponse(BaseModel):
    """
    Fields returned by the OpenWeather API
    that are used in the code
    """

    main: OpenWeatherResponseMain
