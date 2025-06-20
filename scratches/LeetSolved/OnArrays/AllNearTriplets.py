"""
Input: nums

Output: maximum value computed from every triplet such that:
    (nums[i] - nums[k]) * nums[k]  -- 0 triplet_value = 0

triple iteration: O(n^3)
"""


class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fi = 0
        fj = 1
        fk = 2

        s = set()

        while fk < len(nums):
            triplet_value = self.find_triplet(nums[fi], nums[fj], nums[fk])
            if triplet_value < 0:
                triplet_value = 0
            s.add(triplet_value)

            fk += 1
            if fk == len(nums):
                fk = fj + 1
                fj += 1
            if fj == len(nums):
                fj = fi + 1
                fi += 1

        return max(s)

    def find_triplet(self, vi, vj, vk):
        return (vi - vj) * vk

sol = Solution()

print("Test 1:", sol.maximumTripletValue([1, 10, 3, 4]))
print("Test 2:", sol.maximumTripletValue([5, 2, 1, 6, 7]))
print("Test 3:", sol.maximumTripletValue([1, 2, 3]))
print("Test 4:", sol.maximumTripletValue([1, 1, 1, 1]))
print("Test 5:", sol.maximumTripletValue([10, 20, 5, 3]))
