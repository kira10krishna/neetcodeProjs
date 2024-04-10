class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # Create a set to store unique elements of the list
        unique_nums = set()

        # Iterate through the list
        for num in nums:
            # If the number is already in the set, return True
            if num in unique_nums:
                return True
            # Otherwise, add the number to the set
            unique_nums.add(num)

        # If all numbers are unique, return False
        return False
    

if __name__ == "__main__":
    nums = [1,2,3,1]
    print(Solution().containsDuplicate([1,2,2,3,4,4,5]))