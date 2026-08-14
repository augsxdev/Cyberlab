from __future__ import annotations

import json
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).with_name("cyberlab.db")


def connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def initialize() -> None:
    with connection() as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS scans (
            id INTEGER PRIMARY KEY AUTOINCREMENT, target TEXT NOT NULL,
            scanned_at TEXT NOT NULL, result_json TEXT NOT NULL
        )""")


def save_scan(report: dict) -> int:
    with connection() as conn:
        cursor = conn.execute(
            "INSERT INTO scans(target, scanned_at, result_json) VALUES (?, ?, ?)",
            (report["target"], report["scanned_at"], json.dumps(report)),
        )
        return int(cursor.lastrowid)


def recent_scans(limit: int = 20) -> list[dict]:
    with connection() as conn:
        rows = conn.execute("SELECT id, target, scanned_at, result_json FROM scans ORDER BY id DESC LIMIT ?", (limit,)).fetchall()
    return [{**dict(row), "result": json.loads(row["result_json"])} for row in rows]
