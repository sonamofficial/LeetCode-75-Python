class Solution(object):
    def gcdOfStrings(self, str1: str, str2: str) ->str:
        if str1 + str2 != str2 + str1:
            return ""
        a = len(str1)
        b = len(str2)
        while b:
            remainder = a % b
            a = b
            b = remainder
        return str1[:a]

# Taking input from the user
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
solution = Solution()
result = solution.gcdOfStrings(str1, str2)
print("Greatest common divisor of the strings:", result)