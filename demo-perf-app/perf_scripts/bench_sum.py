import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__))) 

import time
from app.app import sum_numbers

def run():
    start = time.perf_counter()
    sum_numbers()
    duration = time.perf_counter() - start
    print(f"duration_seconds={duration}")

if __name__ == '__main__':
    run()