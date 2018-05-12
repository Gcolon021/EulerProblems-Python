import math
def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i * i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor

def calcFactorial(n):
    if n == 1:
        return 1
    return n * calcFactorial(n-1)
def isPrime(num):
    if num > 1:
        # check if the number is a multiple of 2
        for x in range(2, num):
            if (num % x) == 0:
                return False
        else:
            return True


def largestprimefactor(num):
    primederivative = -1
    if num == 1: return "N/A"
    while num % 2 == 0:
        primederivative = 2
        num = num/2

    upto = int(num**0.5) + 1
    for odd in range(3, upto, 2):
        while num % odd == 0:
            primederivative = odd
            num = num/odd

    primederivative = max(num, primederivative)

    return primederivative

#def isPalindrome(left, right, array):
