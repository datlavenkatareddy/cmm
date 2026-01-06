from reflex_store import update_reflex

update_reflex(
    pattern="RUNTIME_NULL_ERROR",
    action="Check state initialization before render",
    time_ms=180,
    success=True
)

update_reflex(
    pattern="RUNTIME_NULL_ERROR",
    action="Check state initialization before render",
    time_ms=120,
    success=True
)

update_reflex(
    pattern="RUNTIME_NULL_ERROR",
    action="Add optional chaining",
    time_ms=200,
    success=False
)

print("Reflex store updated")
