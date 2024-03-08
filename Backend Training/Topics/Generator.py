# Fibonacci Sequence Generator:
import random

# Write a generator function that generates the Fibonacci sequence indefinitely.


def Fibonacci_generator():
    a = 0
    b = 1
    while True:
        yield a
        a = b
        b = a + b


# fib = Fibonacci_generator()
# for i in range(10):
#     print(next(fib))


# Even Number Generator:
# Write a generator function that generates even numbers up to a given limit.
def even_generator(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i


# for i in even_generator(10):
#     print(i)


# Prime Number Generator:
# Write a generator function that generates prime numbers indefinitely
def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, (n // 2) + 1):
        if n % i == 0:
            return False
    return True


def prime_generator():
    i = 0
    while True:
        if is_prime(i):
            yield i
        i += 1


# prime = prime_generator()
# for i in range(10):
#     print(next(prime))


# Character Counter Generator:
# Write a generator function that counts the occurrences of each character in a given string
def count_generator(string):
    for i in set(string):
        yield (i, string.count(i))


# for i in count_generator("hellohowareyou"):
#     print(i)


# Random Number Generator:
# Write a generator function that generates random numbers within a specified range.
def random_number_generator(l1, l2):
    if l1 > l2:
        return None
    while True:
        yield random.randint(l1, l2)


random_num = random_number_generator(1, 2)
for i in range(10):
    print(next(random_num))
