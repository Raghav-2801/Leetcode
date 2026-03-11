class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0

        for num in nums:
            current = num
            length = 1

            while current + 1 in nums:
                current += 1
                length += 1

            longest = max(longest, length)

        return longest
time: O(n2)
space: O(1)


Optimal 
#I used a hashset for O(1) lookup.
# Instead of expanding from every number, I only start sequences when the number has no predecessor (num-1 not in set).
# This ensures each sequence is processed only once.

def longestConsecutive(nums):
    num_set = set(nums)
    longest = 0

    for num in num_set:

        # start of sequence
        if num - 1 not in num_set:

            length = 1
            current = num

            while current + 1 in num_set:
                current += 1
                length += 1

            longest = max(longest, length)

    return longest
