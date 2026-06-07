class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkIfValid(row: List[str]):
            seen = set()
            for num in row:
                if num == ".":
                    continue
                num = int(num)
                if num in seen or num < 1 or num > 9:
                    return False
                seen.add(num)
            return True
        # check if each row has nums 1-9, no duplicates
        for row in board:
            if not checkIfValid(row):
                return False
        # check if each col is valid
        for i in range(9):
            if not checkIfValid([x[i] for x in board]):
                return False

        # check if each square is valid

        for box_row in range(3):
            for box_col in range(3):
                square = []
                for row in range(box_row * 3, (box_row + 1) * 3):
                    for col in range(box_col * 3, (box_col + 1) * 3):
                        square.append(board[row][col])
                if not checkIfValid(square):
                    return False

        return True






