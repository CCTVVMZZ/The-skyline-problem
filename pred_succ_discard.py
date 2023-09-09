from union_find import UnionFind

class PredSuccDiscard:

    def __init__(self, u):
        self.u = u
        self.uf = UnionFind(u + 1)
        self.max_list = list(range(u)) + [None]
        self.pred_list = [None] + list(range(u))

    def discard(self, key):
        if key < 0 or key >= self.u:
            return
        new_pred = self.pred_list[self.uf.find(key)]
        new_max = self.max_list[self.uf.find(key + 1)]
        self.uf.union(key, key + 1)
        i = self.uf.find(key)
        self.pred_list[i] = new_pred
        self.max_list[i] = new_max

    def succ(self, key):
        if key >= self.u:
            return None
        key = max(key, - 1)
        return self.max_list[self.uf.find(key + 1)]

    def pred(self, key):
        if key <= 0:
            return None
        key = min(key, self.u)
        return self.pred_list[self.uf.find(key)]
        

    def __iter__(self):
        key = self.succ(-1)
        while key is not None:
            yield key
            key = self.succ(key)
        

    


# l = PredSuccDiscard(12)
# print(l.succ(13))
# print(l.succ(12))

# l.discard(5)
# l.discard(6)
# l.discard(7)
# print(l.succ(4))
# print(l.pred(8))
                
            
                
            
        
        

    
