from balance.dto import Host
from balance.abstract import AbstractBalancer


class RoundRobinBalancer(AbstractBalancer):
    def __init__(self, hosts):
        AbstractBalancer.__init__(self, hosts)
        self.next_i: int = 0

    def _move_i(self):
        self.next_i = (self.next_i+1) % len(self.hosts)

    def select_host(self) -> Host:
        i = self.next_i
        self._move_i()
        return self.hosts[i]
