#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.13,<3.14"
# dependencies = [
#   "psycopg[binary]>=3.2,<4",
# ]
# ///


import psycopg

POSTGRES_IMAGE = "postgres:18.6-alpine3.24"
POSTGRES_USER = "demo"
POSTGRES_PASSWORD = "demo"
POSTGRES_DB = "demo"
POSTGRES_PORT = 7123
       
       
connection_string = (
            f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
            f"@127.0.0.1:{POSTGRES_PORT}/{POSTGRES_DB}"
        )

connection1 = psycopg.connect(connection_string, connect_timeout=1)
connection1.execute(
            "TRUNCATE TABLE inventory"
        )
connection1.commit()

connection1.execute(...)