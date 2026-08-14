from __future__ import annotations

from .ports import DEFAULT_PORTS


def describe_port(port: int) -> str:
    return DEFAULT_PORTS.get(port, "Serviço não identificado")
