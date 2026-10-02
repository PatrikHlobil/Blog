#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.13,<3.14"
# dependencies = [
#   "docker>=7.1,<8",
#   "psycopg[binary]>=3.2,<4",
# ]
# ///

from collections.abc import Iterator
from contextlib import contextmanager
import time

import docker
from docker.models.containers import Container
import psycopg

POSTGRES_IMAGE = "postgres:18.6-alpine3.24"
POSTGRES_USER = "demo"
POSTGRES_PASSWORD = "demo"
POSTGRES_DB = "demo"
POSTGRES_PORT = 7123


@contextmanager
def postgres_container() -> Iterator[str]:
    client = docker.from_env()
    container: Container | None = None

    try:
        container = client.containers.run(
            POSTGRES_IMAGE,
            detach=True,
            environment={
                "POSTGRES_USER": POSTGRES_USER,
                "POSTGRES_PASSWORD": POSTGRES_PASSWORD,
                "POSTGRES_DB": POSTGRES_DB,
            },
            ports={"5432/tcp": ("127.0.0.1", POSTGRES_PORT)},
        )
        container.reload()
        host_port = container.attrs["NetworkSettings"]["Ports"]["5432/tcp"][0][
            "HostPort"
        ]
        connection_string = (
            f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
            f"@127.0.0.1:{host_port}/{POSTGRES_DB}"
        )

        deadline = time.monotonic() + 30
        while True:
            try:
                connection = psycopg.connect(connection_string, connect_timeout=1)
                break
            except psycopg.OperationalError:
                if time.monotonic() >= deadline:
                    raise RuntimeError(
                        "PostgreSQL did not become ready within 30 seconds"
                    )
                time.sleep(0.25)

        connection.execute("""
            CREATE TABLE inventory (
                id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
                product text NOT NULL,
                buyer text,
                delivery_address text
            )
            """)
        connection.commit()
        connection.close()
        yield connection_string
    finally:
        if container is not None:
            container.remove(force=True)
        client.close()


def main() -> None:
    try:
        with postgres_container() as connection_string:
            print("PostgreSQL is ready.")
            print(f"Connection URL: {connection_string}")
            print("Press Ctrl+C to stop PostgreSQL and remove the container.")

            try:
                while True:
                    time.sleep(3600)
            except KeyboardInterrupt:
                print("\nStopping PostgreSQL...")
    except KeyboardInterrupt:
        print("\nPostgreSQL startup interrupted.")
    else:
        print("PostgreSQL stopped.")


if __name__ == "__main__":
    main()
