import time

import httpx
from fastapi import FastAPI

app = FastAPI()


# global variable for store cached rate and last time for request
cached_rate = None
last_request_time = None


@app.post("/exchange-rate")
async def get_exchange_rate(source_currency: str, destination_currency: str):
    """This endpoint returns the exchange rate between two currencies"""

    global cached_rate, last_request_time

    # check last request time
    if last_request_time is not None and time.time() - last_request_time < 10:
        return {"rate": cached_rate}

    # making request to external API
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={source_currency}&to_currency={destination_currency}&apikey=V2V43QAQ8RILGBOW"

    async with httpx.AsyncClient() as client:
        response: httpx.Response = await client.get(url)

    # update cached rate and time for last request
    cached_rate = response.json()["Realtime Currency Exchange Rate"][
        "5. Exchange Rate"
    ]
    last_request_time = time.time()

    return {"rate": cached_rate}
