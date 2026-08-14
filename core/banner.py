from __future__ import annotations

import socket


def grab_banner(host: str, port: int, timeout: float = 0.7) -> str | None:
    try:
        with socket.create_connection((host, port), timeout=timeout) as sock:
            sock.settimeout(timeout)
            if port in (80, 443):
                sock.sendall(f"HEAD / HTTP/1.0\r\nHost: {host}\r\n\r\n".encode())
            data = sock.recv(256).decode("utf-8", errors="replace").strip()
            return data[:256] or None
    except OSError:
        return None
