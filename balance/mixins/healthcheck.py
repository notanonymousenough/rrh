import time
import requests
from threading import Thread
from balance.abstract import AbstractBalancer


class HealthCheckMixin(AbstractBalancer):
    def __init__(self, hosts: list[str], method: str, health_uri: str, timeout: float, expected_status: int):
        AbstractBalancer.__init__(self, hosts)
        self.uri: str = health_uri
        self.method: str = method
        self.timeout: float = timeout
        self.expected_status: int = expected_status
        self.running = True
        self.thread = Thread(target=self.checker)
        self.thread.start()

    def checker(self):
        while self.running:
            for host in self.hosts:
                host.active = requests.request(
                    self.method,
                    host.make_url(self.uri),
                    timeout=self.timeout
                ).status_code == self.expected_status
            time.sleep(1)
