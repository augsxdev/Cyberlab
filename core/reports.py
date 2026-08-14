from __future__ import annotations

import csv
import json
from pathlib import Path
from uuid import uuid4

REPORTS_DIR = Path(__file__).resolve().parents[1] / "reports"


def export_report(report: dict, format: str = "json") -> Path:
    REPORTS_DIR.mkdir(exist_ok=True)
    stem = f"scan-{uuid4().hex[:8]}"
    if format == "json":
        output = REPORTS_DIR / f"{stem}.json"
        output.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
        return output
    if format == "txt":
        output = REPORTS_DIR / f"{stem}.txt"
        lines = [f"CyberLab — {report['target']}", f"Data: {report['scanned_at']}", "", "Portas abertas:"]
        lines += [f"- {item['port']} / {item['service']}" for item in report["open_ports"]]
        output.write_text("\n".join(lines), encoding="utf-8")
        return output
    if format == "csv":
        output = REPORTS_DIR / f"{stem}.csv"
        with output.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["port", "service", "banner"])
            writer.writeheader(); writer.writerows(report["open_ports"])
        return output
    raise ValueError("Formato suportado: json, txt ou csv.")
