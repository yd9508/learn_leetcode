class Solution:
    def findKthLargest(self, nums, k):
        """
        The problem is asking for the k th largest element.
        Let's push all the elements onto a min-heap,
        but pop from the heap when the size exceeds k.
        When we pop, the smallest element is removed.
        By limiting the heap's size to k, after handling all elements,
        the heap will contain exactly the kkk largest elements from the array.
        :param nums:
        :param k:
        :return:
        """
        heap = []
        for num in nums:
            heap.heappush(heap, num)
            if len(heap) > k:
                heap.heappop(heap)

        return heap[0]
