from pathlib import Path

import yaml

from blog_generator.models.models import Link
from blog_generator.templates import template_env


def render_links_site(links_filepath: Path, target_dir: Path):
    links = _read_in_links(links_filepath)
    links_template = _get_links_template()
    rendered_links = links_template.render(links=links)
    (target_dir / "links.md").write_text(rendered_links)


def _read_in_links(links_filepath: Path) -> list[Link]:
    links = yaml.safe_load(links_filepath.read_text())
    return [Link(**link) for link in links]


def _get_links_template():
    return template_env.get_template("links.md")
