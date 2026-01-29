from __future__ import annotations

import random
import time
from typing import Dict, List


class Environment:

    DISASTER_TYPES = [
        "earthquake",
        "flood",
        "fire",
        "landslide",
        "storm",
    ]

    LOCATIONS = [
        "Sector-A",
        "Sector-B",
        "Sector-C",
        "Sector-D",
        "Sector-E",
    ]

    def __init__(self, seed: int | None = None):
        self.rng = random.Random(seed)
        self.time = int(time.time())

    def step(self) -> List[Dict]:
        events: List[Dict] = []
        self.time += self.rng.randint(1, 10)

        p_event = 0.35
        if self.rng.random() < p_event:
            for _ in range(self.rng.randint(1, 3)):
                etype = self.rng.choice(self.DISASTER_TYPES)
                severity = self.rng.choice(["low", "medium", "high", "critical"])
                loc = self.rng.choice(self.LOCATIONS)
                event = {
                    "timestamp": self.time,
                    "type": etype,
                    "severity": severity,
                    "location": loc,
                    "description": self._desc_for(etype, severity, loc),
                }
                events.append(event)

        if self.rng.random() < 0.02:
            for loc in self.rng.sample(self.LOCATIONS, 2):
                events.append(
                    {
                        "timestamp": self.time,
                        "type": "multi-hazard",
                        "severity": "critical",
                        "location": loc,
                        "description": "Concurrent hazards detected; immediate response required",
                    }
                )

        return events

    def _desc_for(self, etype: str, severity: str, loc: str) -> str:
        return f"{etype.title()} at {loc} with {severity} severity"


if __name__ == "__main__":
    env = Environment(seed=0)
    for _ in range(5):
        ev = env.step()
        if ev:
            print(ev)
