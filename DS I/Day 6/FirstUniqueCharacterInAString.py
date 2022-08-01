class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)

        for i, c in enumerate(s):
            if count[c] == 1:
                return i

        return -1
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
S
