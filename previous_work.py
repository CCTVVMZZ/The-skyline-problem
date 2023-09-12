from box import Box
from functools import total_ordering

from heapq import heappush, heappop
from collections import namedtuple

from infinity_factory import infinity_factory
from sort_utils import merge_iterables


def boxes_from_edges_and_heights(edges, heights, *, negative_infinity):
    """
    >>> boxes_from_edges_and_heights(list(range(10)), # doctest: +NORMALIZE_WHITESPACE
    ... [- 1, 8, 8, 5, - 1, - 1, 7, 9, 6, - 1],
    ... negative_infinity = - 1) 
    [Box(left=1, height=8, right=3),
     Box(left=3, height=5, right=4),
     Box(left=6, height=7, right=7),
     Box(left=7, height=9, right=8),
     Box(left=8, height=6, right=9)]
    """    
    
    assert len(edges) == len(heights), \
        "The list of edges and the list of heights are of different lengths."
    
    if not edges:
        return []

    result = []
    l = edges[0]
    h = heights[0]
    for i in range(1, len(edges)):

        assert edges[i - 1] <= edges[i], \
            "Edges are not sorted." #
        assert edges[i - 1] != edges[i] or heights[i - 1] == heights[i], \
            "Height inconsistencies." #
        
        if heights[i] != h:
            if negative_infinity != h:
                result.append(Box(l, h, edges[i]))
            l = edges[i]
            h = heights[i]

    assert negative_infinity == h, "The skyline extends indefinitely to the right."
    return result


def edges_and_heights_from_boxes(boxes, *, negative_infinity):
    """
    >>> edges_and_heights_from_boxes([Box(1, 10, 3), Box(3, 10, 4), Box(5, 10, 6), Box(6, 11, 7)],
    ... negative_infinity = -1)
    ([1, 4, 5, 6, 7], [10, -1, 10, 11, -1])
    """
    
    if not boxes:
        return []
    
    edges = [boxes[0].left]
    heights = [boxes[0].height]
    
    for i in range(1, len(boxes)):

        assert boxes[i - 1].right <= boxes[i].left, "Some boxes intersect."
        
        if boxes[i - 1].right < boxes[i].left:
            edges.append(boxes[i - 1].right)
            heights.append(negative_infinity)
        elif boxes[i - 1].height == boxes[i].height:
            continue
        
        edges.append(boxes[i].left)
        heights.append(boxes[i].height)

    edges.append(boxes[-1].right)
    heights.append(negative_infinity)

    return edges, heights
    
        
        

    

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



            
def merge_skylines(sl1, sl2):
    it = merge_iterables(sl1, sl2, key = lambda b: b.left)
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
   
      
def skyline_heapq(boxes):

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

                     
        


        
    # print(edges_and_heights_from_boxes([Box(1, 10, 3),
    #                                     Box(3, 10, 12),
    #                                     Box(13, 15, 14),
    #                                     Box(14, 20, 15),
    #                                     Box(15, 15, 16)],
    #                                    negative_infinity = 0))
    
        
                    
                    
                    
    
        
    


