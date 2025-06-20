
#input: arr
#output: list of subarrays such that sub in subarrays contains all nums.distinctElements

# O(n^2) double for to n

def CompleteSubarrays(nums):

    distincs = set(nums) #efficient distinct

    subs = []
    for start in range(len(nums)):
        for end in range(start, len(nums)):
            sottoarray = nums[start:end + 1]
            subs.append(sottoarray)

    result = []
    for sub in subs:
        if(distincs.issubset(set(sub))):
            result.append(sub)


    return result


nums = [1, 2, 1, 3]
complete_subarrays = CompleteSubarrays(nums)

for sub in complete_subarrays:
    print(sub)
