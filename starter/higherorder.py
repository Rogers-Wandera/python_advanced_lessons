# reduce filter map
from functools import reduce
import time


def calc_Execution_time(func):
    def wrapper(*args, **kwargs):
        starttime = time.time()
        results = func(*args, **kwargs)
        endtime = time.time()
        execution_time = endtime - starttime
        print(
            f"Function {func.__name__} took {execution_time} seconds to execute")
        return results
    return wrapper


@calc_Execution_time
def calculateTotal(array):
    total = 0
    for item in array:
        total += item
    return total


array = [23, 45, 67, 78, 78, 78, 45, 56, 12]
print(calculateTotal(array))

# map
results = map(lambda x: x+1, array)
print(list(results))

# filter
results = filter(lambda x: x % 2 == 0, array)
print(list(results))

# reduce
results = reduce(lambda acc, cur: acc + cur, array, 0)
print(results)

print(sum(array, 10))
