"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""
if __name__ == '__main__':
    y = 20
    found = False
    while not found:
        isMultiple = True
        for x in range(11, 20):
            if not y % x == 0:
                isMultiple = False
                break

        if isMultiple:
            found = True
        y = y+20
    print(y)
