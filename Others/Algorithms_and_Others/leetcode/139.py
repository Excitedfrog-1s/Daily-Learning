class Solution:

    def wordBreak(self, s, wordDict):
        length = len(s)
        dp = [True] + [False] * length
        for i in range(length):
            if dp[i]:
                for j in range(i, length):
                    if s[i:j + 1] in wordDict:
                        dp[j + 1] = True
        return dp[-1]


wordDict = ["leet", "code"]
string = "leetcode"
s = Solution()
result = s.wordBreak(string, wordDict)
print(result)
