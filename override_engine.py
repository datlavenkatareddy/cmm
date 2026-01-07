from reflex_store import load_reflexes

MIN_SEEN_COUNT = 2
MIN_SUCCESS_RATE = 0.8
MAX_OVERRIDE_FAILURES = 2



def should_override(pattern: str):
    reflexes = load_reflexes()

    candidates = []
    for r in reflexes:
        if (
        r["pattern"] == pattern
        and r["seen_count"] >= MIN_SEEN_COUNT
        and r.get("override_failures", 0) < MAX_OVERRIDE_FAILURES
        ):
            success_rate = r["success_count"] / r["seen_count"]
            if success_rate >= MIN_SUCCESS_RATE:
                candidates.append((success_rate, r))

    if not candidates:
        return None

    # choose best reflex (highest success, then fastest)
    candidates.sort(
        key=lambda x: (-x[0], x[1]["avg_time_ms"])
    )

    return candidates[0][1]
