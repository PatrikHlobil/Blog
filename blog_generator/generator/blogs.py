from pathlib import Path

from blog_generator.templates import template_env


def render_blogs(config, target_dir: Path):
    blog_template = _get_blog_template()
    rendered_links = blog_template.render(links=config.links)
    with (target_dir / "blogs.md").open(mode="w") as f:
        f.write(rendered_links)


def _get_blog_template():
    return template_env.get_template("blog.md")


# def _read_in_blog_document(path: )
