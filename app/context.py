from app.yaml_reader import YamlReader
import logging

logger = logging.getLogger(__name__)


class AppContext:
    def __init__(self, config_path: str):
        self.yaml: YamlReader = YamlReader(config_path)
        self.hosts = []

    async def on_startup(self, app=None):
        config = self.yaml.parse()
        logger.info(f"Read config: {config}")
        self.hosts = config["hosts"]

    async def on_shutdown(self, app=None):
        pass
