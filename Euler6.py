"""
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

if __name__ == '__main__':
    sumOfSquare = 0
    squareOfSum = 0
    for x in range(1, 101):
        sumOfSquare += x**2
        squareOfSum += x
    print(squareOfSum**2 - sumOfSquare)
