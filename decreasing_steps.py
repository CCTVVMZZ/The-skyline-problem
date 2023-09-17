from heapq import heappush, heappop, heapify
from previous_work import boxes_from_edges_and_heights
from van_emde_boas import VanEmdeBoasTree  
from sort_utils import MaxHeap




class DecreasingSteps_heapq:

    def __init__(self, iterable1 = None, iterable2 = None):
        if iterable1 is None:
            iterable = []
        elif iterable2 is None:
            iterable = iterable1 
        else:
            iterable =  zip(iterable1, iterable2)
        self.data = MaxHeap( ((x, y) for x, y in iterable), key = lambda t: t[1] )

    def __bool__(self):
        return bool(self.data)

    def get_top(self):
        x, y = self.data.pop_max()
        
        while self and self.data.peek_max()[1] >= y:
            other_x, _ = self.data.pop_max()
            if x < other_x:
                x = other_x

        self.data.push((x, y)) # we have to put the toothpaste back in the tube
        
        return x, y

    def pop_top(self):
        
        top = self.get_top()
                
        while self and self.data.peek_max()[0] <= top[0]:
            self.data.pop_max()
            
        return top 

    def add(self, x, y):
        self.data.push((x, y))

        
class DecreasingSteps_vEB:

    def __init__(self, u):

        self.vEB = VanEmdeBoasTree(u.bit_length())
        self.ys = [ None ] * u  # None is used as a placeholder

    def __bool__(self):
        return bool(self.vEB)

    def get_top(self):
        x = self.vEB.min
        return x, self.ys[x]

    def pop_top(self):
        top = self.get_top()
        self.vEB.discard(top[0])
        return top        

    def add(self, x, y):
        vEB = self.vEB
        ys = self.ys
        if x in vEB and y <= ys[x]:
            return
        s = vEB.succ(x)
        if s is not None and ys[s] >= y:
            return    
        p = vEB.pred(x)
        while p is not None and ys[p] <= y:
            vEB.discard(p)
            p = vEB.pred(p)
        ys[x] = y
        vEB.add(x)

def skyline_steps(boxes):

    boxes = list(boxes)

    if not boxes:
        return boxes

    boxes.sort( key = lambda b: b.left )
    
    neg_inf = object()
    
    steps = DecreasingSteps_vEB( 1 +  max ( b.right for b in boxes ) )
    i = 0
    edges = []
    heights = []
    
    while i < len(boxes):

        l = boxes[i].left

        while steps and steps.get_top()[0] <= l:
            x, y = steps.pop_top()
            edges.append(x)
            heights.append(y)

        if not edges or edges[-1] < l:
            edges.append(l)
            if steps:
                heights.append(steps.get_top()[1])
            else:
                heights.append(neg_inf)
           
        while i < len(boxes) and boxes[i].left <= l:
            steps.add(boxes[i].right, boxes[i].height)
            i += 1

    while steps:
        x, y = steps.pop_top()
        edges.append(x)
        heights.append(y)

    heights.pop(0)
    heights.append(neg_inf)

    # return edges, heights
    return boxes_from_edges_and_heights(edges, heights, negative_infinity = neg_inf)
            

# from box import Box
# test = [ [0, 21, 4], [4, 17, 11], [4, 17, 24], [11, 12, 12], [12, 9, 16], [16, 5, 21], [21, 3, 24], [24, 1, 30] ]
# test = [ Box(*b) for b in test ]
# #print(skyline_steps(test))

# d = DecreasingSteps_vEB(12)
# # d.add(0, 1090)
# # d.add(1, 1080)
# # d.add(2, 1070)
# # d.add(3, 1060)
# d.add(4, 1050)
# d.add(4, 1075)
# d.add(6, 2001)
# d.add(5, 2000)

# # d.add(5, 1040)
# # d.add(6, 1030)

# # print(d.pop_top())
# # print(d.pop_top())
# # print(d.pop_top())
# print(d.pop_top())
# #print(d.pop_top())




