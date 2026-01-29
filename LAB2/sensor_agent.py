from __future__ import annotations

import asyncio
import json
import logging
import os
from datetime import datetime

from environment import Environment


LOG_PATH = os.path.join(os.path.dirname(__file__), "events.log")


class SensorAgent:
    def __init__(self, env: Environment, interval: float = 2.0):
        self.env = env
        self.interval = interval
        logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
        self.logger = logging.getLogger("SensorAgent")

    async def run(self, cycles: int | None = None):
        i = 0
        self.logger.info("SensorAgent started")
        while cycles is None or i < cycles:
            events = self.env.step()
            if events:
                for e in events:
                    self._record(e)
                    self.logger.info(f"Detected event: {e['type']} {e['severity']} @ {e['location']}")
            await asyncio.sleep(self.interval)
            i += 1
        self.logger.info("SensorAgent finished")

    def _record(self, event: dict):
        event_copy = dict(event)
        event_copy["observed_at"] = datetime.utcfromtimestamp(event_copy["timestamp"]).isoformat() + "Z"
        with open(LOG_PATH, "a", encoding="utf-8") as fh:
            fh.write(json.dumps(event_copy) + "\n")


async def main():
    env = Environment()
    agent = SensorAgent(env, interval=1.0)
    await agent.run(cycles=8)


if __name__ == "__main__":
    asyncio.run(main())