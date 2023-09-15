from functools import total_ordering
from heapq import heappush, heappop, heapify
from collections import namedtuple
from previous_work import boxes_from_edges_and_heights
from infinity_factory import infinity_factory

    
class MaxHeap:

    @total_ordering
    class MaxHeapItem(namedtuple("_RawHeapItem", ["key", "value"])):

        # python's heapq module deals with binary MIN-heaps.
        # Since we need a MAX-heap, some inequalities need to be reversed 

        def __lt__(self, other):
            return self.key > other.key  # no bug !!!
        
    def __init__(self, data = None, key = lambda x: x):
        if data is None:
            self.data = []
        else:
            self.data = [ self.MaxHeapItem(key = key(value), value = value) for value in data ]
            heapify(self.data)
            
        self.key = key

    def __len__(self):
        return len(self.data)

    def peek_max(self):
        return self.data[0].value 

    def pop_max(self):
        return heappop(self.data).value

    def push(self, value):
        heappush(self.data, self.MaxHeapItem(key = self.key(value), value = value))

h = MaxHeap([3, 7, 1])
h.push(5)
print(h.pop_max())
print(h.peek_max())
print(h.pop_max())
print(h.pop_max())
print(h.pop_max())

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

def skyline_steps(boxes):

    boxes = list(boxes)

    if not boxes:
        return boxes

    boxes.sort( key = lambda b: b.left )
    
    neg_inf = object()
    
    steps = DecreasingSteps_heapq()
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

# d = decreasing_steps_heapq()
# d.add(0, 1090)
# d.add(1, 1080)
# d.add(2, 1070)
# d.add(3, 1060)
# d.add(4, 1050)
# d.add(4, 1075)
# d.add(5, 1040)
# d.add(6, 1030)

# print(d.pop_top())
# print(d.pop_top())
# print(d.pop_top())
# print(d.pop_top())
# print(d.pop_top())


