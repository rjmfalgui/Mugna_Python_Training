import time


def time_decorator(func):
    def time_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        end_time = time.perf_counter()
        final_time = end_time - start_time
        result = final_time * 1000
        print(f"Time executed: {result:.5f}s.")
        return func(*args, **kwargs)
    return time_wrapper

@time_decorator
def adding_function(x,y):
    print(f"The sum is {x+y}.")
adding_function(3,5)