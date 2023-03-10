from pathlib import Path

import click

from blog_generator.generator.links import render_links_site

RELATIVE_LINK_PATH = "links.yaml"


@click.command()
@click.option(
    "--content-dir", type=click.Path(exists=True, path_type=Path), required=True
)
@click.option("--target-dir", type=click.Path(path_type=Path), required=True)
def generate_content(content_dir: Path, target_dir: Path):
    render_links_site(
        links_filepath=content_dir / RELATIVE_LINK_PATH, target_dir=target_dir
    )
