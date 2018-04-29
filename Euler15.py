"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly
6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
George Colon Jr
4/29/18

Notes: After some trail and error I realised the problem is a combonation problem; however the factorials are to
large to calculate. Drawing out a 2 by 2 lead me to realize it is a pascal triangle and I can use
C(n,k+1) = C(n,k) * (n-k) / (k+1)
and itterate through the values instead of using a factorial to calculate the problem
"""
from MathFunctions import calcFactorial
def main():
    print(pascal(20))
    #This will return a list of value which will be needed to multiple together to solve the problem?
    #I think this the solution
    pass

def pascal(n):
    line = [1]
    for k in range(n):
        line.append(line[k]*(n-k)/(k+1))
    return line

if __name__ == '__main__':
    main()
