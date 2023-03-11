from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterator

import markdown

from blog_generator.templates import template_env


@dataclass
class BlogData:
    file_name: str
    content: str
    date: datetime
    categories: list[str]
    draft: bool


def render_blogs(blogs_directory: Path, target_dir: Path):
    _prepare_target_directory(target_dir)
    for blog_data in _get_blog_data(blogs_directory):
        if blog_data.draft is False:
            _render_and_export_blog(blog_data, target_dir)


def _render_and_export_blog(blog_data: BlogData, target_dir: Path):
    blog_template = _get_blog_template()
    rendered_blog = blog_template.render(blog_data=blog_data)
    (target_dir / blog_data.file_name).write_text(rendered_blog)


def _prepare_target_directory(target_dir: Path):
    target_dir.mkdir(exist_ok=True)
    for path in target_dir.glob("*.md"):
        path.unlink()


def _get_blog_data(blogs_directory: Path) -> Iterator[BlogData]:
    markdown_processor = markdown.Markdown(extensions=["meta"])
    for blog_path in blogs_directory.glob("*.md"):
        markdown_processor.convert(blog_path.read_text())
        yield BlogData(
            file_name=blog_path.name,
            content="\n".join(markdown_processor.lines),
            date=datetime.strptime(markdown_processor.Meta["date"][0], "%Y-%m-%d"),
            categories=markdown_processor.Meta["categories"],
            draft=False
            if "draft" not in markdown_processor.Meta
            else markdown_processor.Meta["draft"],
        )


def _get_blog_template():
    return template_env.get_template("blog.md")
