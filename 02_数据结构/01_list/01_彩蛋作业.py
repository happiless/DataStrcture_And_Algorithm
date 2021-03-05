class Solution:

    def getNext(self, x: int):
        z = 0
        while x:
            z += (x % 10) ** 2
            x //= 10
        return z

    def isHappy(self, n: int) -> bool:
        p = self.getNext(n)
        q = self.getNext(self.getNext(n))
        while p != q and q != 1:
            p = self.getNext(p)
            q = self.getNext(self.getNext(q))
        return q == 1


if __name__ == '__main__':
    result = 0
    solution = Solution()
    for i in range(100001):
        if solution.isHappy(i):
            result += i
    print(result)
