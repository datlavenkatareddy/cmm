from cmm_engine import handle_input

# Fake reasoning
def reasoning(_):
    return "Check state initialization before render"

# Fake execution: fail override deliberately
def execute_fail(action):
    print("Executing:", action)
    return False  # simulate failure

# Run twice to trigger ban
for i in range(3):
    result = handle_input(
        "TypeError: Cannot read properties of undefined (reading 'map')",
        reasoning_fn=reasoning,
        execute_fn=execute_fail
    )
    print(result)
