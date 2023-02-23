from pathlib import Path

from blog_generator.models.models import Config
from blog_generator.templates import template_env


def render_links_site(config: Config, target_dir: Path):
    links_template = _get_links_template()
    rendered_links = links_template.render(links=config.links)
    with (target_dir / "links.md").open(mode="w") as f:
        f.write(rendered_links)


def _get_links_template():
    return template_env.get_template("links.md")
