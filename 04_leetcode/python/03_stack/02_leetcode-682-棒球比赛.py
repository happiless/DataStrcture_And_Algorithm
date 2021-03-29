from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        res = []
        for x in ops:
            if x == '+':
                r1 = int(res.pop())
                r2 = 0
                if len(res):
                    r2 = int(res.pop())
                    res.append(str(r2))
                    res.append(str(r1))
                    res.append(str(r1 + r2))
                else:
                    res.append(str(r1))

            elif x == 'D':
                r = res.pop()
                res.append(r)
                res.append(2 * int(r))
            elif x == 'C':
                res.pop()
            else:
                res.append(x)
        s = 0
        while res:
            r = int(res.pop())
            s += r
        return s