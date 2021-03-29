class Solution:

    def backspaceCompare(self, S: str, T: str) -> bool:
        s = []
        t = []
        for i in S:
            print(s)
            if i == '#' and s:
                s.pop()
            if i != '#':
                s.append(i)
        for i in T:
            print(t)
            if i == '#' and t:
                t.pop()
            if i != '#':
                t.append(i)
        return s == t