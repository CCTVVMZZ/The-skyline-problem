from box import Box
from previous_work import skyline_quadratic, skyline_DAC, skyline_heapq
from skyline_union_find import skyline_union_find

test_set = {
    "consecutive":
    [[0, 2, 1], [1, 3, 2], [2, 2, 3], [3, 2, 4]],
    "stairway to heaven":
    [[0, 1, 4], [1, 2, 4], [2, 3, 4], [3, 4, 4]],
    "stairway from heaven":
    [[0, 4, 1], [0, 3, 2], [0, 2, 3], [0, 1, 4]],
    "flat":
    [[0, 1, 4], [1, 1, 5], [2, 1, 6], [3, 1, 7]],
    "tall":
    [[0, 1, 1], [0, 3, 1], [0, 4, 1], [0, 2, 1]],
    "leetcode 1":
    [[2, 10, 9], [3, 15, 7], [5, 12, 12], [15, 10, 20], [19, 8, 24]],
    "leetcode 2":
    [[0, 3, 2], [2, 3, 5]],
    "Udi Manber":
    [[1, 11, 5], [2, 6, 7], [3, 13, 9], [12, 7, 16], [14, 3, 25], [19, 18, 22], [23, 13, 29], [24, 4, 28]],
    "sparse":
    [[0, 1, 1], [2, 2, 3], [4, 3, 5], [6, 4, 7]],
    "pyramid":
    [[0, 1, 7], [1, 2, 6], [2, 3, 5], [3, 4, 4]],
    "battlement":
    [[0, 2, 2], [1, 1, 8], [3, 2, 4], [5, 2, 6], [7, 2, 9]],
    "4 pilars and 3 bridges":
    [[0, 3, 2], [1, 2, 5], [3, 1, 10], [4, 3, 6], [7, 3, 9], [8, 2, 12], [11, 3, 13]],
    }

decreasing_steps = [ [0, 21, 4], [4, 17, 11], [11, 12, 12], [12, 9, 16], [16, 5, 21], [21, 3, 24], [24, 1, 30] ]

for name in test_set:
    boxes = test_set[name] = [ Box(*b) for b in test_set[name] ]
    if skyline_quadratic(boxes) \
        == skyline_DAC(boxes) \
        == skyline_heapq(boxes) \
        == skyline_union_find(boxes):            
        print("OK", name)
    else:
        print("ERROR", name)


    

    # print(name)
    # print(skyline_DAC(boxes))
    # print(skyline_union_find(boxes))
    
    # print(skyline_quadratic(boxes) == skyline_DAC(boxes) == skyline_right(boxes), name)
