class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        res = [1]
        p3 = p5 = p7 = 0
        while len(res) < k:
            ans3 = res[p3] * 3
            ans5 = res[p5] * 5
            ans7 = res[p7] * 7
            ans = min(ans3, ans5)
            ans = min(ans, ans7)
            if ans == ans3: p3 += 1
            if ans == ans5: p5 += 1
            if ans == ans7: p7 += 1
            res.append(ans)
        return res[k - 1]