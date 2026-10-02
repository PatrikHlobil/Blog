#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.13,<3.14"
# dependencies = [
#   "psycopg[binary]>=3.2,<4",
#   "rich"
# ]
# ///


import psycopg
from rich import print

POSTGRES_USER = "demo"
POSTGRES_PASSWORD = "demo"
POSTGRES_DB = "demo"
POSTGRES_PORT = 7123


connection_string = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
    f"@127.0.0.1:{POSTGRES_PORT}/{POSTGRES_DB}"
)

connection1 = psycopg.connect(connection_string, connect_timeout=1)
connection2 = psycopg.connect(connection_string, connect_timeout=1)

connection1.execute("TRUNCATE TABLE inventory")
connection1.commit()

# ①
connection1.execute(
    "INSERT INTO inventory (product) VALUES ('Laptop')",
)
connection1.commit()

# ②
buyer = connection2.execute(
    "SELECT buyer FROM inventory WHERE product='Laptop'",
).fetchone()[0]
print(f"②: Buyer is {buyer}")

# ③
connection1.execute("UPDATE inventory SET buyer='Alice' WHERE product='Laptop'")

# ④
buyer = connection2.execute(
    "SELECT buyer FROM inventory WHERE product='Laptop'",
).fetchone()[0]
print(f"④: Buyer is {buyer} (no dirty read)")

# ⑤
connection1.commit()

# ⑥
buyer = connection2.execute(
    "SELECT buyer FROM inventory WHERE product='Laptop'",
).fetchone()[0]
print(f"⑥: Buyer is {buyer} (read committed)")
