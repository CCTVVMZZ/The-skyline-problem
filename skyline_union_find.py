class UnionFind:
    """
    A textbook implementation of the union-find data structure.
    """
    
    def __init__(self, u):
        self.parent = list(range(u))
        self.rank = [0] * u
    
    def find(self, i):
        "A non-recursive implementation with path compression."
        
        j = i
        while self.parent[i] != i:
            i = self.parent[i]
        while j != i:
            j, self.parent[j] = self.parent[j], i
        return i
            
    def union(self, i, j): 
        self.link(self.find(i), self.find(j))

    def link(self, i, j):
        "Union by rank."

        assert self.parent[i] == i 
        assert self.parent[j] == j
        if self.rank[i] > self.rank[j]:
            self.parent[j] = i
        else:
            self.parent[i] = j
            self.rank[j] += self.rank[i] == self.rank[j]
    
    def __iter__(self):
        return (self.find(i) for i in range(len(self.parent)))


class PredSuccDiscard:

    def __init__(self, u):
        self.u = u
        self.uf = UnionFind(u + 1)
        # The ground set of the union-find data structure stored in self.uf
        # contains u as an element.
        # That element is used as a sentinel.
        # It cannot be discarded.
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
        if key < 0:
            return self.max_list[self.uf.find(0)]
        return self.max_list[self.uf.find(key + 1)]

    def pred(self, key):
        if key <= 0:
            return None
        return self.pred_list[self.uf.find(min(key, self.u))]
    
    def __iter__(self):
        key = self.succ(-1)
        while key is not None:
            yield key
            key = self.succ(key)
        
    def __contains__(self, key):
        if key < 0 or key >= self.u:
            return False
        return self.max_list[self.uf.find(key)] == key

    
from sort_utils import counting_sort
from box import Box        
from previous_work import boxes_from_edges_and_heights

        
def skyline_union_find(boxes):
    boxes = list(boxes)
    if not boxes:
        return 
    span = max(b.right for b in boxes)
    heights = [ - 1 ] * (span + 1)
    to_do = PredSuccDiscard(span)
    for b in reversed(counting_sort(boxes, key = lambda b : b.height)):
        i = to_do.succ(b.left - 1)
        while i is not None and i < b.right:
            heights[i] = b.height
            to_do.discard(i)
            i = to_do.succ(i)

    return boxes_from_edges_and_heights(range(span + 1),  heights, negative_infinity = - 1)            

# print(skyline_union_find([Box(1, 2, 3), Box(5, 6, 7)]))
# print(skyline_union_find([Box(1, 2, 10), Box(5, 6, 7)]))

    

    
                
            
        
        

    
