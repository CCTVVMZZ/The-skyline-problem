class UnionFind:
    """
    As textbook implementation of the union-find data structure.
    """
    
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
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
    
    def __str__(self):
        return str([self.find(i) for i in range(len(self.parent))])

    

class DynamicCC:
    
    def __init__(self, n):
        self.uf = UnionFind(n)
        self.contains = [False] * n
        self.stop = list(range(1, n + 1))

    def __len__(self):
        return len(self.contains)

    def union(self, i, j):
        i = self.uf.find(i)
        j = self.uf.find(j)
        self.uf.link(i, j)
        k = self.uf.find(i)
        self.stop[k] = max(self.stop[i], self.stop[j])        

    def next_stop(self, i):
        return self.stop[self.uf.find(i)]
    
    def add(self, i, j):
        k = i
        result = []
        while k < j:
            if not self.contains[k]: result.append(k)
            self.union(i, k)
            self.contains[k] = True
            k = self.next_stop(k)
        if i > 0 and self.contains[i - 1]: self.union(i - 1, i)
        if j < len(self) and self.contains[j]: self.union(i, j)
        return result
    
    def __iter__(self):
        i = 0
        while i < len(self):
            if self.contains[i]:
                j = self.next_stop(i)
                yield i, j
                i = j
            else:
                i += 1
                
import collections
Building = collections.namedtuple("Building", ["left", "height", "right"])

def skyline_uf(buildings):
    span = max(b.right for b in buildings)
    cc = DynamicCC(span)
    result = [0] * span
    for b in sorted(buildings, key = lambda b: b.height, reverse = True): 
        # The latter sort can be implemented in
        # O(max(b.height for b in buildings)) 
        # time if all the .height's are non-negative integers.
        for i in cc.add(b.left, b.right): result[i] = b.height
    return result 
        
cc = DynamicCC(10)
print(cc.add(1, 4))
print(cc.add(6, 9))
print(list(cc))
print(cc.add(2, 8))
cc = DynamicCC(10)
print(cc.add(2, 3))
print(cc.add(5, 6))
print(cc.add(7, 8))
print(list(cc))
print(cc.add(3, 7))
print(list(cc))

import json 
test_set = json.load(open("test-skyline.json"))
    

def skyline_quadratic(buildings):
    res = [0] * max(b.right for b in buildings)
    for b in buildings:
        for i in range(b.left, b.right):
            res[i] = max(res[i], b.height)
    return res

def print_skyline(sl, ground_level = "|", concrete = "*"):
    for h in sl:
        print(ground_level + concrete * h)

for name, buildings in test_set.items():
    print(name)
    buildings = [Building(*b) for b in buildings]
    print_skyline(skyline_uf(buildings))
    assert skyline_uf(buildings) == skyline_quadratic(buildings)

            
            
        
        
        
        
