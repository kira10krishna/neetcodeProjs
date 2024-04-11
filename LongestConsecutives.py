class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        # Handle empty list
        if not nums:
            return 0

        # Initialize an empty set to store unique numbers
        unique_nums = set(nums)

        # Initialize a variable to store the maximum length
        max_length = 0

        # Iterate over the unique numbers
        for num in unique_nums:
            # Skip if the number is not the start of a sequence
            if num - 1 not in unique_nums:
                # Initialize a variable to store the current length
                current_length = 1

                # Iterate while the next number is in the set
                while num + 1 in unique_nums:
                    num += 1
                    current_length += 1

                # Update the maximum length
                max_length = max(max_length, current_length)

        return max_length