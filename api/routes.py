from __future__ import annotations

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field, field_validator

from core.network import discover_hosts
from core.reports import export_report
from core.scanner import scan_host
from core.utils import is_safe_target
from database.models import recent_scans, save_scan

router = APIRouter()


class ScanRequest(BaseModel):
    target: str = Field(examples=["192.168.1.10"])
    ports: list[int] | None = Field(default=None, max_length=100)
    timeout: float = Field(default=0.35, ge=0.05, le=3)
    consent: bool = Field(description="Confirma que você tem autorização para testar o alvo.")

    @field_validator("ports")
    @classmethod
    def valid_ports(cls, ports: list[int] | None) -> list[int] | None:
        if ports and any(port < 1 or port > 65535 for port in ports):
            raise ValueError("Portas devem estar entre 1 e 65535.")
        return ports


@router.get("/health")
def health() -> dict:
    return {"status": "ok"}


@router.post("/scan")
def scan(request: ScanRequest) -> dict:
    if not request.consent or not is_safe_target(request.target):
        raise HTTPException(403, "O CyberLab só permite alvos privados/loopback com autorização explícita.")
    try:
        report = scan_host(request.target, request.ports, request.timeout)
    except ValueError as error:
        raise HTTPException(422, str(error)) from error
    report["id"] = save_scan(report)
    return report


@router.post("/discover")
def discover(target: str, consent: bool) -> dict:
    if not consent or not is_safe_target(target):
        raise HTTPException(403, "Informe uma rede privada autorizada e consent=true.")
    try:
        return {"network": target, "hosts": discover_hosts(target)}
    except ValueError as error:
        raise HTTPException(422, str(error)) from error


@router.get("/history")
def history(limit: int = 20) -> list[dict]:
    return recent_scans(max(1, min(limit, 100)))


@router.post("/reports/{scan_id}/{format}")
def report(scan_id: int, format: str) -> dict:
    scan = next((item for item in recent_scans(1000) if item["id"] == scan_id), None)
    if not scan:
        raise HTTPException(404, "Scan não encontrado.")
    try:
        output = export_report(scan["result"], format)
    except ValueError as error:
        raise HTTPException(422, str(error)) from error
    return {"path": str(output), "format": format}
