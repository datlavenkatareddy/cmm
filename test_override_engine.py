from override_engine import should_override

reflex = should_override("RUNTIME_NULL_ERROR")

if reflex:
    print("Override triggered")
    print("Action:", reflex["action"])
else:
    print("No override, reasoning required")
