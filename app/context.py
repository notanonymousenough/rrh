import logging
import typing as tp
from app.yaml_reader import YamlReader
from balance.abstract import AbstractBalancer

logger = logging.getLogger(__name__)


class AppContext:
    def __init__(self, config_path: str, balancer: tp.Type[AbstractBalancer]):
        self.yaml: YamlReader = YamlReader(config_path)
        self.balancer_class = balancer
        self.balancer: tp.Optional[AbstractBalancer] = None

    async def on_startup(self, app=None):
        config = self.yaml.parse()
        logger.info(f"Read config: {config}")
        self.balancer = self.balancer_class(config["hosts"])

    async def on_shutdown(self, app=None):
        pass
