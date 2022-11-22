"""
1207. Unique Number of Occurrences

Given an array of integers arr, return true if the number of occurrences of each value in the array is unique, or false otherwise.
"""
class Solution:
    def uniqueOccurrences(self, arr):
        dic = {}
        for num in arr:
            if num in dic.keys():
                dic[num]= dic[num] + 1
            else:
                dic[num] = 1

        if len(set(arr)) == len(set(dic.values())):
            return True
        else:
            return False



