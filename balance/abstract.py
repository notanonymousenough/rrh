import abc

from balance.dto import Host


class AbstractBalancer(abc.ABC):
    def __init__(self, hosts: list[str]):
        self.hosts: list[Host] = []
        for host in hosts:
            self.hosts.append(Host(host))

    @abc.abstractmethod
    def select_host(self) -> Host:
        pass
