from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Count the occurrences of each number
        count = Counter(nums)

        # Get the k most frequent numbers
        top_k = count.most_common(k)

        # Return the numbers
        return [num for num, freq in top_k]
    

    if __name__ == '__main__':
        nums = [1,1,1,2,2,3]
        k = 2

        print(topKFrequent(nums, k))