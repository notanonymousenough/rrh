from balance.roundrobin import RoundRobinBalancer
from balance.roundrobinplus import RoundRobinPlusBalancer


class BalancerFactory:
    @staticmethod
    def arg_to_balancer(arg):
        match arg:
            case "rr":
                return RoundRobinBalancer
            case "rr+":
                return RoundRobinPlusBalancer
        raise ValueError("Balancer not found")
