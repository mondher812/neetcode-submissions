class Nodes:
        def __init__(self):
            
            self.isend = False
            self.val = None
            self.children ={}



class WordDictionary:

    def __init__(self):
        self.root = Nodes()
        self.root.isend = False
            
        

    def addWord(self, word: str) -> None:
        cur = self.root
        pointer = 0
        while pointer < len(word):
            if word[pointer] in cur.children:
                cur = cur.children[word[pointer]]
                pointer+=1
            else:
                new_n = Nodes()
                new_n.val = word[pointer]
                cur.children[word[pointer]] = new_n
                cur = new_n
                pointer+=1
        cur.isend = True
         
        

    def search(self, word: str) -> bool:


        def dfs(curr,point):
            if point < len(word):
                char = word[point]
                if char == ".":
                    for child in curr.children:
                        if dfs(curr.children[child],point+1):
                            return True
                    return False
                else:
                    if char not in curr.children:
                        return False
                    return dfs(curr.children[char], point + 1)
            if curr.isend:
                return True
            else:
                return False 
        return dfs(self.root,0)







       \