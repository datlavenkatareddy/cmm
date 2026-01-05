from logger import log_experience

log_experience(
    raw_input="TypeError: Cannot read properties of undefined (reading 'map')",
    pattern="RUNTIME_NULL_ERROR",
    action_taken="Check state initialization before render",
    time_ms=180,
    success=True
)

print("Experience logged successfully")
