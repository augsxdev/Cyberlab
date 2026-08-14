from __future__ import annotations

import socket


def lookup(hostname: str) -> list[str]:
    try:
        return sorted({entry[4][0] for entry in socket.getaddrinfo(hostname, None)})
    except socket.gaierror:
        return []
