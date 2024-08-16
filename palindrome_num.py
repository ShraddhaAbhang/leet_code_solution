'''
Question: Palindrom Number


Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?

'''

# Solution:

def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    if x < 10:
        return True
    string = str(x)
    print(string)
    # y = len(string)
    temp2 = len(string)//2
    for i in range(temp2):
        if string[i]!=string[-(i+1)]:
            return False
        if i == temp2 - 1:
            return True
        

# ---------------------------------------------------------------------------------------------------------------------

# Another approach:

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Early return for negative numbers and numbers ending with 0 (but not 0 itself)
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        # Revert half of the number to compare
        reverted_number = 0
        while x > reverted_number:
            reverted_number = reverted_number * 10 + x % 10
            x //= 10
        
        # Check if the original number is equal to the reverted number
        # For odd-digit numbers, discard the middle digit by reverted_number // 10
        return x == reverted_number or x == reverted_number // 10

'''
Explanation:
Negative and Edge Case Check:

If the number is negative, it cannot be a palindrome (x < 0).
If the number ends with 0 but is not 0, it cannot be a palindrome (e.g., 10, 100).
Reverting Half of the Number:

We revert only half of the number to avoid unnecessary comparisons.
By comparing the first half of the digits with the reversed second half, we can check for palindrome without converting the number to a string.
Efficiency:

The solution works in O(log10(n)) time complexity because we are processing only half of the digits.
Handling Odd and Even Digits:

For odd-digit numbers, the middle digit doesn't affect the palindrome property, so we discard it by dividing the reverted number by 10.
This approach avoids string conversion and provides a more optimal solution for checking if a number is a palindrome.

'''