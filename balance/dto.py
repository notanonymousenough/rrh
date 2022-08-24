from dataclasses import dataclass
from urllib.parse import urljoin


@dataclass
class Host:
    name:  str
    active: bool = True

    def make_url(self, uri):
        return urljoin(self.name, uri)

