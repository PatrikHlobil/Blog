from pathlib import Path

import click

from blog_generator.generator.links import render_links_site
from blog_generator.models.validate import parse_config


@click.command()
@click.option(
    "--content-dir", type=click.Path(exists=True, path_type=Path), required=True
)
@click.option(
    "--target-dir", type=click.Path(exists=True, path_type=Path), required=True
)
def generate_html(content_dir: Path, target_dir: Path):
    config = parse_config(content_dir)
    render_links_site(config, target_dir)
