from box import Box
from collections import namedtuple
from functools import total_ordering
from heapq import heappush, heappop
from infinity_factory import infinity_factory

    
def boxes_from_edges_and_heights(edges, heights, *, negative_infinity):
    
    assert len(edges) == len(heights) # debug
    
    if not edges:
        return []

    result = []
    l = edges[0]
    h = heights[0]
    for i in range(1, len(edges)):
        if heights[i] != h:
            if negative_infinity != h:
                result.append(Box(l, h, edges[i]))
            l = edges[i]
            h = heights[i]            
    return result
    

def skyline_quadratic(boxes):
    boxes = tuple(boxes)
    edges = [ b.left for b in boxes ] + [ b.right for b in boxes ]
    n = len(edges)
    edges.sort()

    negative_infinity, _ = infinity_factory()

    heights = [ negative_infinity ] * n
    for i in range(n):
        for b in boxes:
            if b.left <= edges[i] < b.right:
                heights[i] = max(b.height, heights[i])

    return boxes_from_edges_and_heights(edges, heights, negative_infinity = negative_infinity)



def merge_sorted(it1, it2, /, *, key = lambda x: x):
    it1 = iter(it1)
    it2 = iter(it2)
    try:
        x1 = next(it1)
    except StopIteration:
        yield from it2
        return
    try:
        x2 = next(it2)
    except StopIteration:
        yield x1
        yield from it1
        return
    k1 = key(x1)
    k2 = key(x2)
    while True:
        if k1 <= k2:
            yield x1
            try:
                x1 = next(it1)
            except StopIteration:
                yield x2
                yield from it2
                return
            k1 = key(x1)
        else:
            k1, k2 = k2, k1
            x1, x2 = x2, x1
            it1, it2 = it2, it1

            
def merge_skylines(sl1, sl2):
    it = merge_sorted(sl1, sl2, key = lambda b: b.left)
    result = []
    
    try: 
        last = next(it)
    except StopIteration:
        return [last]
            
    for b in it:
        *more, last = skyline_quadratic([last, b])
        result.extend(more)
    return result + [last]

            
def skyline_DAC(boxes): # Divide And Conquer 
    boxes = tuple(boxes)
    n = len(boxes) 
    if n <= 1:
        return boxes
    n //= 2
    return merge_skylines(skyline_DAC(boxes[:n]), skyline_DAC(boxes[n:]))


            
@total_ordering
class MaxHeapItem(namedtuple("_RawHeapItem", ["key", "value"])):

    # python's heapq module deals with binary MIN-heaps.
    # Since we need a MAX-heap, some inequalities need to be reversed 

    def __lt__(self, other):
        return self.key > other.key # no bug !!!
   
      
def skyline_right(boxes):

    boxes = list(boxes)

    if not boxes:
        return boxes
    
    neg_inf, pos_inf = infinity_factory()

    boxes.sort(key = lambda b: b.left )
    
    active_boxes = []
    i = 0
    edges = []
    heights = []
    e = boxes[0].left # edge e is the sweep line 

    while pos_inf > e:
        
        while i < len(boxes) and boxes[i].left <= e:
            heappush(active_boxes, MaxHeapItem(key = boxes[i].height, value = boxes[i].right))
            # the ith box is now active because it straddles e
            i += 1

        while active_boxes and active_boxes[0].value <= e:  # comparison of 
            heappop(active_boxes) # removing stragglers

        h, r = active_boxes[0] if active_boxes else (neg_inf, pos_inf)
        edges.append(e)
        heights.append(h)
        e = l if i < len(boxes) and r > (l := boxes[i].left) else r 
        
    return boxes_from_edges_and_heights(edges, heights, negative_infinity = neg_inf)

                     
        

if __name__ == "__main__":
    from json import load
    test_set = load(open("test-skyline.json"))
    for name in test_set:
        boxes = test_set[name] = [ Box(*b) for b in test_set[name] ]
        assert skyline_quadratic(boxes) == skyline_DAC(boxes) == skyline_right(boxes)
        # print(skyline_quadratic(boxes) == skyline_DAC(boxes) == skyline_right(boxes), name)

        
    
        
                    
                    
                    
    
        
    


