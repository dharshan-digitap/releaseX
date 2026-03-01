from typing import Dict

from confluence import ConfluenceHandler
from pr_body import PR_BODY_TEMPLATE
import yaml


class Parser:

    @staticmethod
    def parse_pr_body(_data: str) -> Dict[str, str]:
        content = _data.split("```yaml")[1].split("```")[0]
        return yaml.safe_load(content)


if __name__ == "__main__":
    data = Parser().parse_pr_body(PR_BODY_TEMPLATE)
    ConfluenceHandler().process(
        _data=data,
        release_name="ReleaseX",
    )
