# 7) Decorators Task
#    - Create a decorator called "log_time" that:
#         - Records the execution time of any function.
#         - Saves the function name and runtime into "execution_log.txt".
#    - Apply this decorator to at least two tasks (e.g., Math Automation & Regex Log Cleaner).
#    - Verify that the log file contains entries after running.

import functools
import time


def log_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kargs):
        st = time.time()
        res = func(*args, **kargs)
        end = time.time()
        duration = round(end - st, 4)
        with open("excution_log.txt", "a") as file:
            file.write(f"{func.__name__} ran in {duration} seconds\n")
        return res
    return wrapper
