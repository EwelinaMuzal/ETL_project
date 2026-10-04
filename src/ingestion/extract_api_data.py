import requests
import logging
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


#https://api.frankfurter.dev/v1/2024-01-01..2026-09-21?base=PLN&symbols=EUR,USD
def extract_exchange_rates():
    
    try:
        response = requests.get(
        "https://api.frankfurter.dev/v1/2024-01-01..2026-09-21",
        params = {"base":"PLN", 
                "symbols":"EUR,USD"},
        timeout = 5
    )

        response.raise_for_status()
        data = response.json()
        return data

    except requests.exceptions.RequestException as error:
        logger.error(f"{error}")
        return None

if __name__=="__main__":
    result = extract_exchange_rates()

    with open("data/raw_local/api/exchange_rates.json", "w") as file:
        json.dump(result,file)

    logger.info(result)