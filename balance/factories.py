from balance.roundrobin import RoundRobinBalancer


class BalancerFactory:
    @staticmethod
    def arg_to_balancer(arg):
        match arg:
            case "rr":
                return RoundRobinBalancer
        raise ValueError("Balancer not found")
