class Solution:
    def longestCommonPrefix(self, strs):
        ans = ""
        for i in range(len(strs[0])):
            temp = ans + strs[0][i]
            for string in strs:
                if temp != string[0:(i + 1)]:
                    return ans
            ans = temp

        return ans

if __name__ == '__main__':
    Solution().longestCommonPrefix(["flower","flow","flight"])
