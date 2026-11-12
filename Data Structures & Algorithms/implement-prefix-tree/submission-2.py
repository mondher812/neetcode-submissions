class Nodes:
        def __init__(self):
            
            self.isend = False
            self.val = None
            self.children ={}
class PrefixTree:

    def __init__(self):

        self.root = Nodes()
        self.root.isend = False
    
        

    def insert(self, word: str) -> None:
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
        cur = self.root
        for char in word:
            if char in cur.children:
                cur = cur.children[char]
            else:
                return False
        if cur.isend:
            return True
        else:
            return False 

        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            if char in cur.children:
                cur = cur.children[char]
            else:
                return False
        return len(cur.children) != 0 or cur.isend
        
        