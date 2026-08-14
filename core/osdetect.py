from __future__ import annotations

import platform


def local_os() -> dict[str, str]:
    return {"system": platform.system(), "release": platform.release(), "version": platform.version()}
