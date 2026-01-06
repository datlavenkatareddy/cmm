from patterns import extract_pattern

tests = [
    "TypeError: Cannot read properties of undefined (reading 'map')",
    "ImportError: No module named 'numpy'",
    "python is not recognized as an internal or external command",
    "some random error message"
]

for t in tests:
    print(t, "->", extract_pattern(t))
