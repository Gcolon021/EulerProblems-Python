"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
def isPalindrome(left, right, array):
    if left+1 == right+1 and array[left] == array[right]:
        return True
    if left + 1 == right and array[left] == array[right]:
        return True
    if array[left] == array[right]:
        return isPalindrome(left+1, right-1, array)
    return False

if __name__ == '__main__':
    answer = 0
    for x in range(100, 999):
        for y in range(999, 100, -1):
            num = [int(z) for z in str(x*y)]
            if isPalindrome(0, len(num)-1, num):
                if x*y > answer:
                    answer = x*y
    print(answer)
