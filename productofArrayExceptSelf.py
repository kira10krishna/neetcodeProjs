class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # Initialize the result list with all elements set to 1
        result = [1] * len(nums)

        # Calculate the product of all elements before the current element
        product = 1
        for i in range(len(nums)):
            result[i] *= product
            product *= nums[i]

        # Calculate the product of all elements after the current element
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= product
            product *= nums[i]

        # Return the result list
        return result
    

if __name__=='__main__':
    nums = [1,2,3,4]
    print(Solution().productExceptSelf(nums))