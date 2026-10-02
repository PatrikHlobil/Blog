#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.13,<3.14"
# dependencies = [
#   "psycopg[binary]>=3.2,<4",
#   "rich"
# ]
# ///


from concurrent.futures import ThreadPoolExecutor

import psycopg
from rich import print

POSTGRES_IMAGE = "postgres:18.6-alpine3.24"
POSTGRES_USER = "demo"
POSTGRES_PASSWORD = "demo"
POSTGRES_DB = "demo"
POSTGRES_PORT = 7123


connection_string = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
    f"@127.0.0.1:{POSTGRES_PORT}/{POSTGRES_DB}"
)


def setup_inventory_table() -> None:
    with psycopg.connect(connection_string, connect_timeout=1) as connection:
        connection.execute("TRUNCATE TABLE inventory")
        connection.commit()


def create_inventory_item(product: str) -> None:
    with psycopg.connect(connection_string, connect_timeout=1) as connection:
        inventory_item = connection.execute(
            "SELECT * FROM inventory WHERE product=%s", (product,)
        ).fetchone()
        if inventory_item:
            print(f"Product {product} already exists in inventory.")
            return

        # Simulate business logic execution time:
        connection.execute("INSERT INTO inventory (product) values (%s)", (product,))
        connection.commit()


def insert_product() -> None:
    create_inventory_item(product="Laptop")


if __name__ == "__main__":
    setup_inventory_table()

    executor = ThreadPoolExecutor(max_workers=2)
    t1 = executor.submit(insert_product)
    t2 = executor.submit(insert_product)

    while True:
        if t1.done() and t2.done():
            break

    with psycopg.connect(connection_string, connect_timeout=1) as connection:
        products = connection.execute(
            "SELECT * FROM inventory WHERE product='Laptop'"
        ).fetchall()
        print(f"Found {len(products)} 'Laptops'!")
