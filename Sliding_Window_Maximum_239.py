from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        You are given an array of integers nums,
        there is a sliding window of size k which is moving from the very left of the array to the very right.
        You can only see the k numbers in the window. Each time the sliding window moves right by one position.

        Return the max sliding window.

        My solution, "Time Limit Exceeded" O(N^2)
        :param nums:
        :param k:
        :return:
        """
        ans = []
        head = 0
        tail = k
        while tail <= len(nums):
            ans.append(max(nums[head:tail]))
            head += 1
            tail += 1

        return ans

    def maxSlidingWindow2(self, nums, k):
        """
        O(N)
        :param nums:
        :param k:
        :return:
        """
        dq = deque()
        res = []

        for i in range(k):
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)

        res.append(nums[dq[0]])

        for i in range(k, len(nums)):
            if dq and dq[0] == i - k:
                dq.popleft()
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()

            dq.append(i)
            res.append(nums[dq[0]])

        return res


