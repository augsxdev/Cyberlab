from __future__ import annotations

import socket
from concurrent.futures import ThreadPoolExecutor, as_completed

DEFAULT_PORTS = {
    21: "FTP", 22: "SSH", 23: "Telnet", 53: "DNS", 80: "HTTP", 110: "POP3",
    139: "NetBIOS", 143: "IMAP", 443: "HTTPS", 445: "SMB", 3389: "RDP",
}


def scan_port(host: str, port: int, timeout: float = 0.35) -> dict | None:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            if sock.connect_ex((host, port)) == 0:
                return {"port": port, "service": DEFAULT_PORTS.get(port, "unknown")}
    except OSError:
        pass
    return None


def scan_ports(host: str, ports: list[int], timeout: float = 0.35, workers: int = 30) -> list[dict]:
    workers = max(1, min(workers, 100))
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = [pool.submit(scan_port, host, port, timeout) for port in sorted(set(ports))]
        open_ports = [future.result() for future in as_completed(futures) if future.result()]
    return sorted(open_ports, key=lambda item: item["port"])
