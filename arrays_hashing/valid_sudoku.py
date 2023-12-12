class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Line by line comparison
        # Horizontal check
        for i in range(len(board)):
            used_already = [False for i in range(10)]
            for j in board[i]:
                if j == '.':
                    continue
                if used_already[int(j)] is True:
                    return False
                used_already[int(j)] = True

        # Vertical check
        for i in range(len(board)):
            used_already = [False for i in range(10)]
            for j in range(len(board)):
                if board[j][i] == '.':
                    continue
                if used_already[int(board[j][i])] is True:
                    return False
                used_already[int(board[j][i])] = True

        # Box by box check
        horizontal = 3
        vertical = 3
        for boxes in range(9):
            if horizontal == 12:
                horizontal = 3
                vertical += 3
            
            horiz_i = horizontal - 3
            vert_i = vertical - 3
            used_already = [False for i in range(10)]

            while vert_i < vertical:
                horiz_i = horizontal - 3
                while horiz_i < horizontal:
                    print(f'horiz: {horiz_i}')
                    print(f'vert: {vert_i}')
                    print(board[vert_i][horiz_i])
                    if board[vert_i][horiz_i] == '.':
                        horiz_i += 1
                        continue
                    if used_already[int(board[vert_i][horiz_i])] is True:
                        return False
                    used_already[int(board[vert_i][horiz_i])] = True

                    horiz_i += 1
                vert_i += 1
            
            horizontal += 3
            boxes += 1

        
        return True
