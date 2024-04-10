class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Create an empty dictionary to store the indices of the numbers
        num_indices = {}

        # Iterate through the numbers in the input list
        for i, num in enumerate(nums):
            # Calculate the difference between the target and the current number
            diff = target - num

            # Check if the difference is in the dictionary
            if diff in num_indices:
                # If it is, return the indices of the current number and the difference
                return [num_indices[diff], i]

            # If the difference is not in the dictionary, add the current number and its index to the dictionary
            num_indices[num] = i

        # If no pair of numbers sums up to the target, return an empty list
        return []
    
if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9

    print(Solution().twoSum(nums, target))