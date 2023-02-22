from pathlib import Path

import click
import yaml

from blog_generator.models.models import Config


@click.command()
@click.argument("config-dir", type=click.Path(exists=True, path_type=Path))
def main(config_dir: Path):
    validate_config(config_dir)


def validate_config(config_dir: Path) -> Config:
    config = dict()
    config["links"] = yaml.safe_load((config_dir / "links.yaml").read_text())
    return Config(**config)
