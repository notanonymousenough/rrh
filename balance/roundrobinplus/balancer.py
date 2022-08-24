from balance.dto import Host
from balance.roundrobin import RoundRobinBalancer
from balance.mixins import HealthCheckMixin


class RoundRobinPlusBalancer(RoundRobinBalancer, HealthCheckMixin):
    def __init__(self, hosts: list[str], method: str = "GET", health_uri: str = "/", timeout: int = 10, expected_status: int = 200):
        RoundRobinBalancer.__init__(self, hosts)
        HealthCheckMixin.__init__(self, hosts, method, health_uri, timeout, expected_status)
        self.next_i: int = 0

    def _move_i(self):
        self.next_i = (self.next_i+1) % len(self.hosts)
        if not self.hosts[self.next_i].active:
            self._move_i()

    def select_host(self) -> Host:
        i = self.next_i
        self._move_i()
        return self.hosts[i]
