import datetime
from pathlib import Path

from bs4 import BeautifulSoup
import click
import requests
import yaml

LINK_CONFIG_FILE = Path(__file__).parent.parent.parent / "content" / "links.yaml"


@click.command()
@click.argument("https_link")
@click.option(
    "--link-config-file",
    required=False,
    default=LINK_CONFIG_FILE,
    type=click.Path(exists=True, path_type=Path, file_okay=True),
)
def add_link(https_link: str, link_config_file: Path):
    with open(link_config_file, encoding="utf-8") as f:
        link_config = yaml.safe_load(f)

    response = requests.get(https_link)
    response.raise_for_status()
    content = BeautifulSoup(response.text, "html.parser")

    link = dict(
        title=str(content.title.string),
        authors=["???"],
        tags=[],
        link=https_link,
        date=datetime.date.today(),
    )
    link_config.append(link)

    with open(link_config_file, "w", encoding="utf-8") as f:
        yaml.safe_dump(link_config, f, sort_keys=False, indent=2, allow_unicode=True)
