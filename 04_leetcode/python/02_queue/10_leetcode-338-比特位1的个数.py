from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        """
        x & (x - 1) x比特位最后一位的1变成0
        :param num:
        :return:
        """
        res = [0 for _ in range(num + 1)]
        for i in range(1, num + 1):
            res[i] = res[i & (i - 1)] + 1
        return res