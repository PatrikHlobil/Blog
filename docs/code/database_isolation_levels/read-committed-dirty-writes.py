#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.13,<3.14"
# dependencies = [
#   "psycopg[binary]>=3.2,<4",
#   "rich"
# ]
# ///


from concurrent.futures import ThreadPoolExecutor
import time

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


def log(statement: str) -> None:
    run_time = time.time() - start_time
    print(f"{run_time:.2f} Seconds | {statement}")


def setup_inventory_table() -> None:
    with psycopg.connect(connection_string, connect_timeout=1) as connection:
        connection.execute("TRUNCATE TABLE inventory")

        # ①
        connection.execute("INSERT INTO inventory (product) VALUES ('Laptop')")
        connection.commit()


def update_from_user_1() -> None:
    with psycopg.connect(connection_string, connect_timeout=1) as connection:
        # ③
        connection.execute("UPDATE inventory SET buyer='Alice' WHERE product='Laptop'")
        log("User 1: UPDATE inventory SET buyer='Alice' WHERE product='Laptop'")

        # Try to wait for User 2 to apply changes (will be blocked by DB lock!)
        time.sleep(2)

        # ⑦
        connection.execute(
            "UPDATE inventory SET delivery_address='Los Angeles' WHERE product='Laptop'"
        )
        log(
            "User 1: UPDATE inventory SET delivery_address='Los Angeles' WHERE product='Laptop'"  # noqa: E501
        )

        # ⑧
        connection.commit()


def update_from_user_2() -> None:
    with psycopg.connect(connection_string, connect_timeout=1) as connection:
        # Wait for User 1 to make first change ③:
        time.sleep(1)

        # ④
        connection.execute("UPDATE inventory SET buyer='Robin' WHERE product='Laptop'")
        log("User 2: UPDATE inventory SET buyer='Robin' WHERE product='Laptop'")

        # ⑤
        connection.execute(
            "UPDATE inventory SET delivery_address='New York' WHERE product='Laptop'"
        )
        log(
            "User 2: UPDATE inventory SET delivery_address='New York' WHERE product='Laptop'"  # noqa: E501
        )

        # ⑥
        connection.commit()


if __name__ == "__main__":
    start_time = time.time()
    setup_inventory_table()

    executor = ThreadPoolExecutor(max_workers=2)
    executor.submit(update_from_user_1)
    executor.submit(update_from_user_2)

    time.sleep(3)

    with psycopg.connect(connection_string, connect_timeout=1) as connection:
        row = connection.execute(
            "SELECT buyer, delivery_address FROM inventory WHERE product='Laptop'"
        ).fetchone()
        if row is None:
            raise RuntimeError("Laptop not found")
        print(f"Final buyer is {row[0]}, delivery address is {row[1]}")
