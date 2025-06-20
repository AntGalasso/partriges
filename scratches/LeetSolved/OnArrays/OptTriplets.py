def maximumTripletValue(nums):
    maxDiff, maxTriplet, maxElement = 0

    for num in nums:
        maxTriplet = max(maxTriplet, maxDiff * num)
        maxDiff = max(maxDiff, maxElement - num)
        maxElement = max(maxElement, num)
    return maxTriplet


"""
leet code 2874

fittable

class Solution(object):
    def maximumTripletValue(self, nums):
        maxTriplet, maxElement, maxDiff = 0, 0, 0
        for num in nums:
            maxTriplet = max(maxTriplet, maxDiff * num)
            maxDiff = max(maxDiff, maxElement - num)
            maxElement = max(maxElement, num)
        return maxTriplet

    O(n^3)



solution for O(n)

    one pass 
        longest met so far
        longest difference. foreach (i, j) met store i-j ? this > ab

        combine triplets - save the longest

    grant i < j < k 




"""