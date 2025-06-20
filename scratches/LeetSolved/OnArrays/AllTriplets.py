"""
    solution of maximum triplet value on the other way of iteration
    O(n^3)



"""

class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    value = self.find_triplet(nums[i], nums[j], nums[k])
                    if value < 0:
                        value = 0

                    s.add(value)

        return max(s)

    def find_triplet(self, vi, vj, vk):
        return (vi - vj) * vk

