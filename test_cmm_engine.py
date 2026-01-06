from cmm_engine import handle_input


def slow_reasoning(raw_input):
    # simulate thinking
    return "Check state initialization before render"


result = handle_input(
    "TypeError: Cannot read properties of undefined (reading 'map')",
    reasoning_fn=slow_reasoning
)

print(result)
