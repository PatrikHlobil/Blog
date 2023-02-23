import os.path

from jinja2 import Environment, FileSystemLoader, select_autoescape

template_env = Environment(
    loader=FileSystemLoader(os.path.dirname(__file__)), autoescape=select_autoescape()
)
