class Solution:
    def countSegments(self, s: str) -> int:
        cnt = 0
        for i in range(len(s)):
            if (i==0 or s[i-1] == ' ') and s[i] != ' ':
                cnt += 1
        return cnt
