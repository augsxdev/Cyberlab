from __future__ import annotations

from .alerts import evaluate
from .banner import grab_banner
from .hostname import resolve_hostname
from .ports import DEFAULT_PORTS, scan_ports
from .utils import normalize_target, utc_now


def scan_host(target: str, ports: list[int] | None = None, timeout: float = 0.35) -> dict:
    host = normalize_target(target).split("/")[0]
    selected_ports = ports or list(DEFAULT_PORTS)
    open_ports = scan_ports(host, selected_ports, timeout=timeout)
    for item in open_ports:
        item["banner"] = grab_banner(host, item["port"])
    return {
        "target": host,
        "hostname": resolve_hostname(host),
        "scanned_at": utc_now(),
        "open_ports": open_ports,
        "alerts": evaluate(open_ports),
    }
