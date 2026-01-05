import json
import time
from pathlib import Path

EXPERIENCE_FILE = Path("experiences.json")


def log_experience(
    raw_input: str,
    pattern: str,
    action_taken: str,
    time_ms: int,
    success: bool
):
    experience = {
        "timestamp": time.time(),
        "raw_input": raw_input,
        "pattern": pattern,
        "action_taken": action_taken,
        "time_ms": time_ms,
        "success": success
    }

    if EXPERIENCE_FILE.exists():
        with open(EXPERIENCE_FILE, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append(experience)

    with open(EXPERIENCE_FILE, "w") as f:
        json.dump(data, f, indent=2)
