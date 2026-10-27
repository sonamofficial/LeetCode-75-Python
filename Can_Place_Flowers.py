class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        if n == 0:
            return True
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                count += 1
                if count >= n:
                    return True
        return False

# Taking input from the user
flowerbed = list(map(int, input("Enter the flowerbed (0s and 1s) separated by spaces: ").split()))
n = int(input("Enter the number of flowers to place: "))
solution = Solution()
result = solution.canPlaceFlowers(flowerbed, n)
print("Can place flowers:", result)