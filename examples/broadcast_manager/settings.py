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
    panel_message_keys: list[str] = field(default_factory=list)
    gap_seconds: float = 15.0
    scan_gap_seconds: float = 3.0
    retry_attempts: int = 6
    retry_rate_limits: bool = True
    show_scan_progress: bool = True
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
            decoded: Any = json.loads(self.path.read_text(encoding="utf-8"))
        except (FileNotFoundError, ValueError, TypeError):
            return Settings()
        if not isinstance(decoded, dict):
            return Settings()
        raw: dict[str, Any] = decoded
        allowed = Settings.__dataclass_fields__.keys()
        try:
            settings = Settings(
                **{key: value for key, value in raw.items() if key in allowed}
            )
            # Keep hand-edited settings within conservative API-friendly bounds.
            settings.gap_seconds = min(
                600.0, max(10.0, float(settings.gap_seconds))
            )
            settings.scan_gap_seconds = min(
                30.0, max(3.0, float(settings.scan_gap_seconds))
            )
            settings.retry_attempts = min(10, max(6, int(settings.retry_attempts)))
            settings.retry_rate_limits = bool(settings.retry_rate_limits)
            settings.show_scan_progress = bool(settings.show_scan_progress)
            settings.interval_minutes = min(
                60, max(1, int(settings.interval_minutes))
            )
            group_ids = (
                settings.group_ids if isinstance(settings.group_ids, list) else []
            )
            settings.group_ids = list(dict.fromkeys(map(str, group_ids)))
            panel_keys = (
                settings.panel_message_keys
                if isinstance(settings.panel_message_keys, list)
                else []
            )
            settings.panel_message_keys = list(
                dict.fromkeys(map(str, panel_keys))
            )[-20:]
        except (TypeError, ValueError):
            return Settings()
        return settings

    def save(self, settings: Settings) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        temporary = self.path.with_suffix(".tmp")
        temporary.write_text(
            json.dumps(asdict(settings), ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        temporary.replace(self.path)
