"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
from Functions import isPrime
if __name__ == '__main__':
    x = 2
    i = 0
    while i < 10001:
        if isPrime(x):
            print(x)
            i += 1
        x += 1
