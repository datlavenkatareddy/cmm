# cmm_engine.py
# Minimal Computational Muscle Memory loop

import time

# ---- Reflex Store (in-memory, minimal) ----
REFLEX_THRESHOLD = 3
reflex_store = {}  # pattern -> {"count": int, "action": str}


# ---- Reasoning (same as baseline, but internal) ----
def reason(error):
    time.sleep(0.01)  # simulate reasoning latency
    if error == "RUNTIME_NULL_ERROR":
        return "Check state initialization before render"
    return "Unknown action"


# ---- Single CMM Step ----
def cmm_step(error):
    start = time.time()

    # Pattern extraction (trivial, rule-based)
    pattern = error

    # Check for reflex
    if pattern in reflex_store and reflex_store[pattern]["count"] >= REFLEX_THRESHOLD:
        action = reflex_store[pattern]["action"]
        mode = "OVERRIDE"
    else:
        action = reason(error)
        mode = "REASONING"

        # Update reflex store
        if action != "Unknown action":
            if pattern not in reflex_store:
                reflex_store[pattern] = {"count": 0, "action": action}
            reflex_store[pattern]["count"] += 1

    time_ms = int((time.time() - start) * 1000)

    return {
        "mode": mode,
        "pattern": pattern,
        "action": action,
        "time_ms": time_ms,
    }
