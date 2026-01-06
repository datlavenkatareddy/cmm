from logger import log_experience
from patterns import extract_pattern

raw_error = "TypeError: Cannot read properties of undefined (reading 'map')"

pattern = extract_pattern(raw_error)

log_experience(
    raw_input=raw_error,
    pattern=pattern,
    action_taken="Check state initialization before render",
    time_ms=180,
    success=True
)

print("Logged with extracted pattern:", pattern)
