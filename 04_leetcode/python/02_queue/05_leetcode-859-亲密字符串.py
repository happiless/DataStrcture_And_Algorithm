class Solution:

    def has_repeate(self, a: str) -> bool:
        cnt = [0 for _ in range(26)]
        for i in range(len(a)):
            cnt[ord(a[i]) - ord('a')] += 1
            if cnt[ord(a[i]) - ord('a')] == 2: return True
        return False

    def buddyStrings(self, a: str, b: str) -> bool:
        if len(a) != len(b): return False
        print(a)
        if a == b: return self.has_repeate(a)
        i = 0
        while a[i] == b[i]: i += 1
        j = i + 1
        while j < len(a) and a[j] == b[j]: j += 1
        if j == len(a) or a[i] != b[j] or a[j] != b[i]: return False
        j += 1
        while j < len(a):
            if a[j] != b[j]: return False
            j += 1
        return True
