import json
import os
import random
import time
from datetime import datetime


LOG_PATH = os.path.join(os.path.dirname(__file__), "events.log")


def make_event(seed_rng):
    types = ["earthquake", "flood", "fire", "storm", "landslide"]
    places = ["Sector-A", "Sector-B", "Sector-C", "Sector-D", "Sector-E"]
    severities = ["low", "medium", "high", "critical"]

    ev = {}
    ev["time"] = int(time.time())
    ev["type"] = seed_rng.choice(types)
    ev["severity"] = seed_rng.choice(severities)
    ev["place"] = seed_rng.choice(places)
    ev["note"] = f"{ev['type'].title()} at {ev['place']} ({ev['severity']})"
    return ev


class SimpleAgent:
    def __init__(self, seed=None, log_path=None):
        self.rng = random.Random(seed)
        self.log_path = log_path or LOG_PATH

    def perceive_and_record(self, steps=5, delay=1.0):
        with open(self.log_path, "a", encoding="utf-8") as fh:
            for i in range(steps):
                if self.rng.random() < 0.35:
                    count = self.rng.randint(1, 2)
                    for _ in range(count):
                        ev = make_event(self.rng)
                        ev["observed_at"] = datetime.utcfromtimestamp(ev["time"]).isoformat() + "Z"
                        line = json.dumps(ev)
                        fh.write(line + "\n")
                        print("Agent saw:", ev["note"])
                else:
                    print("Agent saw nothing this step.")
                time.sleep(delay)


def main():
    agent = SimpleAgent(seed=0)
    agent.perceive_and_record(steps=8, delay=0.5)


if __name__ == "__main__":
    main()