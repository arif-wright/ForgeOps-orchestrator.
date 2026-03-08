from __future__ import annotations

import json
import re
import tempfile
from pathlib import Path
from typing import Any


_RUN_ID_PATTERN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$")


class RunRepository:
    """Store run metadata as JSON files in a local runs directory."""

    def __init__(self, runs_dir: str | Path = "runs") -> None:
        self._runs_dir = Path(runs_dir)
        self._runs_dir.mkdir(parents=True, exist_ok=True)

    def save_run(self, run_id: str, data: dict[str, Any]) -> Path:
        file_path = self._run_file(run_id)

        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=self._runs_dir,
            delete=False,
            suffix=".tmp",
        ) as tmp:
            json.dump(data, tmp, ensure_ascii=False, indent=2, sort_keys=True)
            tmp.write("\n")
            tmp.flush()
            temp_path = Path(tmp.name)

        temp_path.replace(file_path)
        return file_path

    def load_run(self, run_id: str) -> dict[str, Any] | None:
        file_path = self._run_file(run_id)
        if not file_path.exists():
            return None
        with file_path.open("r", encoding="utf-8") as handle:
            loaded = json.load(handle)
        if not isinstance(loaded, dict):
            raise ValueError(f"Run file must contain a JSON object: {file_path}")
        return loaded

    def list_runs(self) -> list[str]:
        runs: list[str] = []
        for path in sorted(self._runs_dir.glob("*.json")):
            if path.is_file():
                runs.append(path.stem)
        return runs

    def _run_file(self, run_id: str) -> Path:
        if not _RUN_ID_PATTERN.fullmatch(run_id):
            raise ValueError(
                "Invalid run_id. Use 1-128 chars: letters, numbers, '.', '_' or '-'; "
                "must start with letter/number."
            )
        return self._runs_dir / f"{run_id}.json"
