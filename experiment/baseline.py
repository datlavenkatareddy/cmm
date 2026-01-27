# baseline.py
import time

def reason(error):
    time.sleep(0.01)
    if error == "RUNTIME_NULL_ERROR":
        return "Check state initialization before render"
    return "Unknown action"

def run_baseline(error, runs=6):
    times = []
    for _ in range(runs):
        start = time.time()
        action = reason(error)
        success = action == "Check state initialization before render"
        times.append(int((time.time() - start) * 1000))
    return times
