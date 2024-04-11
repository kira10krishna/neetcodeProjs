class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Check rows
        for row in board:
            if not self.isValidUnit(row):
                return False

        # Check columns
        for col in zip(*board):
            if not self.isValidUnit(col):
                return False

        # Check 3x3 sub-boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not self.isValidUnit([board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]):
                    return False

        return True

    def isValidUnit(self, unit: list[str]) -> bool:
        # Create a set to store unique elements of the unit
        unique_elements = set()

        # Iterate through the unit
        for element in unit:
            # If the element is not a digit or is already in the set, return False
            if element == "." or element in unique_elements:
                return False
            # Otherwise, add the element to the set
            unique_elements.add(element)

        # If all elements are digits and are unique, return True
        return True 

if __name__=="__main__":
# Create an instance of the Solution class
solution = Solution()

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]


# Call the isValidSudoku method on the instance
print(solution.isValidSudoku(board))

