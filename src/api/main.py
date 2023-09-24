from typing import Annotated

from fastapi import FastAPI, Query, Request, HTTPException, Depends
from fastapi.responses import RedirectResponse

from src.api.models import TemperatureRecord
from src.db.connection import DBConnectionContext
from src.config import Config


def verify_token(request: Request):
    if not (x_token := request.headers.get("x-token")):
        raise HTTPException(
            status_code=400, detail="x-token not provided in the header!"
        )
    if x_token != Config.APPLICATION_X_TOKEN:
        raise HTTPException(
            status_code=401, detail="Invalid x-token provided in the header!"
        )


app = FastAPI()


@app.get("/")
async def docs_redirect():
    response = RedirectResponse(url="/docs")
    return response


@app.get("/temperature", dependencies=[Depends(verify_token)])
async def get_temperature(
    day: Annotated[
        str,
        Query(
            pattern="^\d{4}-\d{2}-\d{2}$",
            title="Day",
            description="Day in format Y-m-d",
        ),
    ]
) -> list[TemperatureRecord]:
    response = []
    with DBConnectionContext() as db:
        fields = list(TemperatureRecord.schema()["properties"].keys())
        query = f"""
            SELECT {','.join(fields)}
            FROM {Config.TABLE_NAME}
            WHERE DATE(timestamp) = "{day}"
        """
        db.execute(query)
        response = [
            TemperatureRecord(**{fields[i]: row[i] for i in range(len(fields))})
            for row in db.fetchall()
        ]

    return response
