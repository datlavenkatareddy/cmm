from cmm_engine import handle_input

def bad_reasoning(_):
    return "Wrong fix"

# Simulate a failure by manually editing success later
result = handle_input(
    "TypeError: Cannot read properties of undefined (reading 'map')",
    reasoning_fn=bad_reasoning
)

print(result)
