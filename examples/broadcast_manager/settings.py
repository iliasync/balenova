from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any


@dataclass(slots=True)
class Settings:
    banner_text: str | None = None
    banner_chat_id: str | None = None
    banner_message_id: str | None = None
    group_ids: list[str] = field(default_factory=list)
    gap_seconds: float = 15.0
    schedule: str = "interval"
    interval_minutes: int = 60
    daily_time: str = "12:00"
    enabled: bool = False
    next_run: str | None = None

    @property
    def has_banner(self) -> bool:
        return bool(self.banner_text or self.banner_message_id)


class SettingsStore:
    def __init__(self, path: str | Path = "sessions/broadcast-settings.json") -> None:
        self.path = Path(path)

    def load(self) -> Settings:
        try:
            raw: dict[str, Any] = json.loads(self.path.read_text(encoding="utf-8"))
        except (FileNotFoundError, ValueError, TypeError):
            return Settings()
        allowed = Settings.__dataclass_fields__.keys()
        return Settings(**{key: value for key, value in raw.items() if key in allowed})

    def save(self, settings: Settings) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        temporary = self.path.with_suffix(".tmp")
        temporary.write_text(
            json.dumps(asdict(settings), ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        temporary.replace(self.path)
