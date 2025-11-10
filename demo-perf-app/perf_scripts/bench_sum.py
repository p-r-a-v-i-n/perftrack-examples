import time

def fast_sum(n=5_000_000):
    total = 0
    for i in range(n):
        total += i
    return total

def run():
    start = time.perf_counter()
    fast_sum()
    duration = time.perf_counter() - start
    print(f"duration_seconds={duration}")

