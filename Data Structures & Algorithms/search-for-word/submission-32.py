class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        def back(used,need,curx,cury):
            if need == len(word):
                return True
            else:
                if board[curx][cury] == word[need] and need+1 == len(word):
                    return True
                elif board[curx][cury] == word[need]:
                    
                    used.add((curx,cury))
                    if (curx+1,cury) not in used and curx+1<len(board):
                       if back(used,need+1,curx+1,cury):
                            return True
                    if (curx-1,cury) not in used and curx-1>=0:                                
                       if back(used,need+1,curx-1,cury):
                            return True
                    if (curx,cury+1) not in used and cury+1<len(board[0]):
                        if back(used,need+1,curx,cury+1):
                            return True
                    if (curx,cury-1) not in used and cury-1>=0:                                
                        if back(used,need+1,curx,cury-1):
                            return True

                    used.remove((curx,cury))
        for i in range(len(board)):
            for j in range(len(board[0])):
                if back(set(),0,i,j):
                    return True
        return False
