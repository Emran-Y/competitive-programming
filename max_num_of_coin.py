class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        sum = 0

        for i in range(len(piles)// 3,len(piles),2):
            print(i + 1)
            sum+=piles[i]
        return sum
