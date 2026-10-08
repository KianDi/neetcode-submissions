class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]

        boxes = defaultdict(set) # key: (r // 3, c //3 ), value: set of digits


        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue


                box_key = ( r // 3, c // 3)

                if val in rows[r] or val in cols[c] or val in boxes[box_key]:
                    return False
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_key].add(val)
        return True