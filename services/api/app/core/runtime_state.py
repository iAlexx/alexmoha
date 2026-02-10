from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class RuntimeState:
    maintenance_mode: bool = False
    emergency_pause: bool = False
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def set_flags(self, maintenance_mode: bool | None = None, emergency_pause: bool | None = None) -> None:
        if maintenance_mode is not None:
            self.maintenance_mode = maintenance_mode
        if emergency_pause is not None:
            self.emergency_pause = emergency_pause
        self.updated_at = datetime.now(timezone.utc)


runtime_state = RuntimeState()
