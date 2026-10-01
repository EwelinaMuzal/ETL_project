import json
import os
import logging
import psycopg
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

#json_path = "data/generated/orders.json"

def load_orders(json_path):
    with open(json_path, "r") as file:
        data = json.load(file)

    conn = psycopg.connect(
        host="localhost",
        port=5433,
        dbname="source_db",
        user=os.environ["POSTGRES_USER"],
        password=os.environ["POSTGRES_PASSWORD"]
    )

    cur = conn.cursor()

    inserted = 0

    for order in data:
        cur.execute(
            "INSERT INTO orders (order_id, customer_id, order_date, status, currency) VALUES (%s, %s, %s, %s, %s)",
            (order["order_id"], order["customer_id"], order["order_date"], order["status"], order["currency"])
        )
        inserted += 1

    conn.commit()
    cur.close()
    conn.close()

    logger.info(f"Inserted {inserted} orders into source_db.orders")

if __name__ == "__main__":
    load_orders("data/generated/orders.json")