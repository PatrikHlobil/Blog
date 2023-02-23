from pathlib import Path

import yaml

from blog_generator.models.models import Config


def parse_config(content_dir: Path) -> Config:
    config = dict()
    config["links"] = yaml.safe_load((content_dir / "links.yaml").read_text())
    return Config(**config)
