import json
from pathlib import Path

REFLEX_FILE = Path("reflexes.json")


def load_reflexes():
    if REFLEX_FILE.exists():
        with open(REFLEX_FILE, "r") as f:
            return json.load(f)
    return []


def save_reflexes(reflexes):
    with open(REFLEX_FILE, "w") as f:
        json.dump(reflexes, f, indent=2)


def update_reflex(pattern: str, action: str, time_ms: int, success: bool):
    reflexes = load_reflexes()

    for r in reflexes:
        if r["pattern"] == pattern and r["action"] == action:
            r["seen_count"] += 1
            if success:
                r["success_count"] += 1
            r["avg_time_ms"] = (
                (r["avg_time_ms"] * (r["seen_count"] - 1) + time_ms)
                / r["seen_count"]
            )
            save_reflexes(reflexes)
            return

    # new reflex
    reflexes.append({
        "pattern": pattern,
        "action": action,
        "seen_count": 1,
        "success_count": 1 if success else 0,
        "avg_time_ms": time_ms,
        "override_failures": 0
    })

    save_reflexes(reflexes)


def penalize_reflex(pattern: str, action: str):
    reflexes = load_reflexes()

    for r in reflexes:
        if r["pattern"] == pattern and r["action"] == action:
            # penalize by reducing success count
            r["success_count"] = max(0, r["success_count"] - 1)

    save_reflexes(reflexes)


def record_override_failure(pattern: str, action: str):
    reflexes = load_reflexes()

    for r in reflexes:
        if r["pattern"] == pattern and r["action"] == action:
            r["override_failures"] = r.get("override_failures", 0) + 1

    save_reflexes(reflexes)
