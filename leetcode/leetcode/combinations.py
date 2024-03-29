class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def back_track(candidate):
            if len(candidate) == k:
                ans.append(candidate[:])
                return
            last = candidate[-1] if candidate else 0

            for next_last in range(last + 1 , n+1):
                candidate.append(next_last)
                back_track(candidate)
                candidate.pop()
        back_track([])
        return ans