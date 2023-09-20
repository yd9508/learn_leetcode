import bisect
class Solution:
    def maxValue(self, events, k):
        """
        You are given an array of events where events[i] = [startDayi, endDayi, valuei].
        The ith event starts at startDayi and ends at endDayi, and if you attend this event, you will receive a value of valuei.
        You are also given an integer k which represents the maximum number of events you can attend.

        You can only attend one event at a time. If you choose to attend an event, you must attend the entire event.
        Note that the end day is inclusive: that is, you cannot attend two events where one of them starts and the other ends on the same day.

        Return the maximum sum of values that you can receive by attending events.

        DP + DFS + Binary Search
        :param events:
        :param k:
        :return:
        """
        events.sort()
        n = len(events)
        starts = [start for start, end, value in events]
        dp = [[-1] * n for _ in range(k + 1)]

        def dfs(cur_index, count):
            if count == 0 or cur_index == n:
                return 0
            if dp[count][cur_index] != -1:
                return dp[count][cur_index]

            # Find the nearest available event after attending event 0.

            next_index = bisect.bisect_right(starts, events[cur_index][1])
            dp[count][cur_index] = max(dfs(cur_index + 1, count), events[cur_index][2] + dfs(next_index, count - 1))
            return dp[count][cur_index]

        return dfs(0, k)
