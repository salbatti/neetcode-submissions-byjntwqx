class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row
        for i in range(9):
            val=set()
            for j in range(9):
                item=board[i][j]
                if item in val:
                    return False
                elif item !=".":
                    val.add(item)


         # colomn
        for i in range(9):
            val=set()
            for j in range(9):
                item=board[j][i]
                if item in val:
                    return False
                elif item !=".":
                    val.add(item)

        start=[[0,0],[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]]

        for r,c in start:
            val=set()
            for i in range(r,r+3):
                for j in range(c,c+3):
                    item=board[i][j]
                    if item in val:
                        return False
                    elif item !=".":
                        val.add(item)

        return True






