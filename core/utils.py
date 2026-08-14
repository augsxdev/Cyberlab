from __future__ import annotations

import ipaddress
from datetime import UTC, datetime


def utc_now() -> str:
    return datetime.now(UTC).isoformat()


def is_safe_target(target: str) -> bool:
    """Aceita apenas IPv4 privado ou loopback, reduzindo uso indevido."""
    try:
        network = ipaddress.ip_network(target, strict=False)
    except ValueError:
        return False
    return network.is_private or network.is_loopback


def normalize_target(target: str) -> str:
    if not is_safe_target(target):
        raise ValueError("Use somente um IP ou rede privada/loopback autorizada.")
    return str(ipaddress.ip_network(target, strict=False))
