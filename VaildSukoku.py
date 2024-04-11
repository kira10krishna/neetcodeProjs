class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        """
        :type board: List[List[str]]
        :btype: bool
        """
        # Check rows
        for row in board:
            if not self.isValid(row):
                return False

        # Check columns
        for col in zip(*board):
            if not self.isValid(col):
                return False

        # Check sub-boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not self.isValid([board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]):
                    return False

        return True

    def isValid(self, nums):
        """
        :type nums: List[str]
        :btype: bool
        """
        return len(nums) == len(set(nums)) and all(num!= '.' for num in nums)