import yaml


class YamlReader:
    def __init__(self, path: str):
        super().__init__()
        self.path = path

    def parse(self):
        with open(self.path) as f:
            return yaml.safe_load(f)
