class Solution:
    def isScramble(self, s1, s2):
        """
        We can scramble a string s to get a string t using the following algorithm:
        If the length of the string is 1, stop.
        If the length of the string is > 1, do the following:
        Split the string into two non-empty substrings at a random index, i.e., if the string is s, divide it to x and y where s = x + y.
        Randomly decide to swap the two substrings or to keep them in the same order. i.e., after this step, s may become s = x + y or s = y + x.
        Apply step 1 recursively on each of the two substrings x and y.
        Given two strings s1 and s2 of the same length, return true if s2 is a scrambled string of s1, otherwise, return false.
        DP solution:
        How do we check whether a given string t is a scrambled string of s? First,
        we choose an index and cut s into x and y (s = x + y).
        Then, we see if we can cut t into x' and y' (t = x' + y' if we do not swap or t = y' + x' if we do).
        Since verifying that x' is a scrambled x and y' is scrambled y are smaller subproblems,
        we will solve the problem using dynamic programming.

        We have two strings s1 and s2.
        For each given dp state, we need 3 variables: length, i, and j.
        Each state will focus on two substrings.
        The first one will be a substring of s1, starting at index i with length equal to length - let's call this substring s.
        The second one will be a substring of s2, starting at index j with length - let's call this substring t.
        Let dp[length][i][j] be a boolean representing whether t is a scrambled version of s.
        The base case, as defined by the problem is when length = 1.
        Here we do not have to split strings into smaller ones,
        so we can easily compare the corresponding characters:
        <<dp[length][i][j] is true when s1[i : (i + length)] equals s2[j : (j + length)], and false otherwise>>.
        :param s1:
        :param s2:
        :return:
        """
        n = len(s1)
        dp = [[[False for j in range(n)] for i in range(n)]
              for l in range(n+1)]
        for i in range(n):
            for j in range(n):
                dp[1][i][j] = s1[i] == s2[j]
        for length in range(2, n + 1):
            for i in range(n + 1 - length):
                for j in range(n + 1 - length):
                    for new_length in range(1, length):
                        dp1 = dp[new_length][i]
                        dp2 = dp[length-new_length][i+new_length]
                        dp[length][i][j] |= dp1[j] and dp2[j+new_length]
                        dp[length][i][j] |= dp1[j+length-new_length] and dp2[j]
        return dp[n][0][0]
