from union_find import UnionFind

class PredSuccDiscard:

    def __init__(self, u):
        self.u = u
        self.uf = UnionFind(u)
        self.lasts = list(range(u))
        self.firsts = list(range(u))

    def discard(self, key):
        if key < 0 or key >= self.u:
            return
        i = self.uf.find(key)
        if self.lasts[i] == key:
            if key == self.u - 1:
                self.lasts[i] = None
            else:
                new_first = self.firsts[self.uf.find(key)]
                new_last = self.lasts[self.uf.find(key + 1)]
                self.uf.union(key, key + 1)
                i = self.uf.find(key)
                self.firsts[i] = new_first 
                self.lasts[i] = new_last

    def succ(self, key):
        if key >= self.u - 1:
            return None
        key = max(key, - 1)
        return self.lasts[self.uf.find(key + 1)]

    def pred(self, key):
        if key <= 0:
            return None
        key = min(key, self.u - 1)
        i = self.firsts[self.uf.find(key)] - 1
        return self.lasts[self.uf.find(i)]
        

    def __iter__(self):
        key = self.succ(-1)
        while key is not None:
            yield key
            key = self.succ(key)
        

    


# l = PredSuccDiscard(12)
# print(l.succ(13))
# l.discard(5)
# print(l.succ(4))
# l.discard(6)
# print(l.succ(4))
# l.discard(7)
# print(l.succ(4))
                
            
                
            
        
        

    
