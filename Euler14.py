"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

George Colon Jr
4/29/18
"""

import time
def sequenceEval(n, counter):
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            counter = counter + 1
        else:
            n = (3 * n) + 1
            counter = counter + 1
    return counter


def main():
    start = time.time()
    var = 0
    answer = 0
    for x in range(13, 1000000):
        temp = 1
        counter = sequenceEval(x, temp)
        if var < counter:
            var = counter
            answer = x
    print(answer)
    print("Time: ", time.time() - start)

if __name__ == '__main__':
    main()
