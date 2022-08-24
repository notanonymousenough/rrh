from balance.dto import Host
from balance.abstract import AbstractBalancer


class RoundRobinBalancer(AbstractBalancer):
    def __init__(self, hosts):
        super().__init__(hosts)
        self.last_called_i: int = 0

    def _move_i(self):
        self.last_called_i = (self.last_called_i+1) % len(self.hosts)

    def select_host(self) -> Host:
        i = self.last_called_i
        self._move_i()
        return self.hosts[i]
