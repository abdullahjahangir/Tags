# Function Timer:
# Write a decorator that calculates and prints the time taken by a function to execute.
import time


def Timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(
            f"Function '{func.__name__}' took {end_time - start_time:.4f} seconds to execute."
        )
        return result

    return wrapper


def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}' with arguments {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned {result}")
        return result

    return wrapper


def validate_args(func):
    def wrapper(*args, **kwargs):
        if (
            len(args) != 2
            or not isinstance(args[0], int)
            or not isinstance(args[1], int)
        ):
            raise ValueError("Function arguments must be two integers")
        return func(*args, **kwargs)

    return wrapper


def memoize(func):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper


@validate_args
@logger
@memoize
@Timer
def sum(a, b):
    time.sleep(1)
    return a + b


print(sum(1, 2))


# Argument Validator:
# Write a decorator that validates the arguments passed to a function based on specified criteria.

# Function Logger:
# Write a decorator that logs the input arguments and return value of a function.

# Memoization:
# Write a decorator that caches the return value of a function based on its input arguments, improving performance by avoiding redundant computations.

# Rate Limiter:
# Write a decorator that limits the rate at which a function can be called, preventing it from being called more than a specified number of times within a certain time interval
