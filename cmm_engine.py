import time

from patterns import extract_pattern
from override_engine import should_override
from reflex_store import update_reflex, penalize_reflex, record_override_failure
from logger import log_experience


def handle_input(raw_input: str, reasoning_fn, execute_fn):
    start_time = time.time()

    pattern = extract_pattern(raw_input)
    reflex = should_override(pattern)

    if reflex:
        action = reflex["action"]
        mode = "OVERRIDE"
    else:
        action = reasoning_fn(raw_input)
        mode = "REASONING"

    # EXECUTION HAPPENS HERE (REALITY DECIDES)
    success = execute_fn(action)

    elapsed_ms = int((time.time() - start_time) * 1000)

    log_experience(
        raw_input=raw_input,
        pattern=pattern,
        action_taken=action,
        time_ms=elapsed_ms,
        success=success
    )

    update_reflex(
        pattern=pattern,
        action=action,
        time_ms=elapsed_ms,
        success=success
    )

    if mode == "OVERRIDE" and not success:
        penalize_reflex(pattern, action)
        record_override_failure(pattern, action)

    return {
        "mode": mode,
        "pattern": pattern,
        "action": action,
        "success": success,
        "time_ms": elapsed_ms
    }
