from app import sum_numbers
import time

def run():
    start = time.perf_counter()
    sum_numbers()
    duration = time.perf_counter() - start
    print(f"duration_seconds={duration}")