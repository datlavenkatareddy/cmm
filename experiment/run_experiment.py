# run_experiment.py
from baseline import run_baseline
from cmm_engine import cmm_step

ERROR = "RUNTIME_NULL_ERROR"

print("Baseline (no CMM):")
baseline_times = run_baseline(ERROR)
print(baseline_times)

print("\nWith CMM:")
cmm_times = []
for i in range(6):
    result = cmm_step(ERROR)
    cmm_times.append(result["time_ms"])
    print(result)

print("\nSummary:")
print("Baseline avg:", sum(baseline_times)//len(baseline_times), "ms")
print("CMM avg:", sum(cmm_times)//len(cmm_times), "ms")
