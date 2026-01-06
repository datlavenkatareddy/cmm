# Pattern IDs (frozen vocabulary for v0)

RUNTIME_NULL_ERROR = "RUNTIME_NULL_ERROR"
ASYNC_TIMING_ERROR = "ASYNC_TIMING_ERROR"
IMPORT_ERROR = "IMPORT_ERROR"
ENV_PATH_ERROR = "ENV_PATH_ERROR"
FILE_NOT_FOUND = "FILE_NOT_FOUND"
UNKNOWN = "UNKNOWN"

def extract_pattern(raw_input: str) -> str:
    text = raw_input.lower()

    if "cannot read properties of undefined" in text:
        return RUNTIME_NULL_ERROR

    if "undefined is not a function" in text:
        return RUNTIME_NULL_ERROR

    if "importerror" in text or "no module named" in text:
        return IMPORT_ERROR

    if "file not found" in text or "no such file" in text:
        return FILE_NOT_FOUND

    if "not recognized as an internal or external command" in text:
        return ENV_PATH_ERROR

    return UNKNOWN
