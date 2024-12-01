class Memoize:
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if args in self.cache:
            return self.cache[args]
        result = self.func(*args)
        self.cache[args] = result
        return result

# Example function to be memoized
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)

# Applying the memoize decorator
memoized_factorial = Memoize(factorial)

# Using the memoized function
print(memoized_factorial(5))  # Output: 120
print(memoized_factorial(5)) 