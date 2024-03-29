class Solution:
    def minTaps(self, n: int, ranges):
        """
        There is a one-dimensional garden on the x-axis. The garden starts at the point 0 and ends at the point n.
        (i.e., the length of the garden is n).

        There are n + 1 taps located at points [0, 1, ..., n] in the garden.

        Given an integer n and an integer array ranges of length n + 1 where ranges[i] (0-indexed)
        means the i-th tap can water the area [i - ranges[i], i + ranges[i]] if it was open.

        Return the minimum number of taps that should be open to water the whole garden, If the garden cannot be watered return -1.


        :param n:
        :param ranges:
        :return:
        """
        # Define an infinite value
        INF = int(1e9)

        # Create a list to store the minimum number of taps needed for each position
        dp = [INF] * (n + 1)

        # Initialize the starting position of the garden
        dp[0] = 0

        for i in range(n + 1):
            # Calculate the leftmost position reachable by the current tap
            tap_start = max(0, i - ranges[i])
            # Calculate the rightmost position reachable by the current tap
            tap_end = min(n, i + ranges[i])

            for j in range(tap_start, tap_end + 1):
                # Update with the minimum number of taps
                dp[tap_end] = min(dp[tap_end], dp[j] + 1)

        # Check if the garden can be watered completely
        if dp[n] == INF:
            # Garden cannot be watered
            return -1

        # Return the minimum number of taps needed to water the entire garden
        return dp[n]
