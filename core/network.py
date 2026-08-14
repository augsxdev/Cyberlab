from __future__ import annotations

import ipaddress
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed

from .hostname import resolve_hostname


def _is_online(ip: str, timeout: float) -> bool:
    try:
        with socket.create_connection((ip, 80), timeout=timeout):
            return True
    except OSError:
        return False


def discover_hosts(cidr: str, timeout: float = 0.2, workers: int = 40) -> list[dict]:
    network = ipaddress.ip_network(cidr, strict=False)
    hosts = list(network.hosts())
    if len(hosts) > 254:
        raise ValueError("Para descoberta, escolha uma rede de até 254 hosts.")
    with ThreadPoolExecutor(max_workers=max(1, min(workers, 100))) as pool:
        futures = {pool.submit(_is_online, str(ip), timeout): str(ip) for ip in hosts}
        found = [
            {"ip": ip, "hostname": resolve_hostname(ip)}
            for future, ip in futures.items() if future.result()
        ]
    return sorted(found, key=lambda host: tuple(map(int, host["ip"].split("."))))
