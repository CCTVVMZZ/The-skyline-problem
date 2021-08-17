{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "069473d3",
   "metadata": {},
   "source": [
    "https://leetcode.com/problems/the-skyline-problem/\n",
    "https://doi.org/10.1145/321906.321910"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a2a64ae9",
   "metadata": {},
   "outputs": [],
   "source": [
    "import collections\n",
    "Building = collections.namedtuple(\"Building\", [\"left\", \"height\", \"right\"])\n",
    "Point2d = collections.namedtuple(\"Point2d\", [\"x\", \"y\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "9aceb705",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'consecutive': {'in': [Building(left=0, height=2, right=1), Building(left=1, height=3, right=2), Building(left=2, height=2, right=3), Building(left=3, height=2, right=4)], 'out': [Point2d(x=0, y=2), Point2d(x=1, y=3), Point2d(x=2, y=2), Point2d(x=4, y=0)]}, 'stairway to heaven': {'in': [Building(left=1, height=1, right=5), Building(left=2, height=2, right=5), Building(left=3, height=3, right=5), Building(left=4, height=4, right=5)], 'out': [Point2d(x=1, y=1), Point2d(x=2, y=2), Point2d(x=3, y=3), Point2d(x=4, y=4), Point2d(x=5, y=0)]}, 'stairway from heaven': {'in': [Building(left=1, height=4, right=2), Building(left=1, height=3, right=3), Building(left=1, height=2, right=4), Building(left=1, height=1, right=5)], 'out': [Point2d(x=1, y=4), Point2d(x=2, y=3), Point2d(x=3, y=2), Point2d(x=4, y=1), Point2d(x=5, y=0)]}, 'flat': {'in': [Building(left=1, height=1, right=5), Building(left=2, height=1, right=6), Building(left=3, height=1, right=7), Building(left=4, height=1, right=8)], 'out': [Point2d(x=1, y=1), Point2d(x=8, y=0)]}, 'tall': {'in': [Building(left=1, height=1, right=2), Building(left=1, height=3, right=2), Building(left=1, height=4, right=2), Building(left=1, height=2, right=2)], 'out': [Point2d(x=1, y=4), Point2d(x=2, y=0)]}, 'leetcode 1': {'in': [Building(left=2, height=10, right=9), Building(left=3, height=15, right=7), Building(left=5, height=12, right=12), Building(left=15, height=10, right=20), Building(left=19, height=8, right=24)], 'out': [Point2d(x=2, y=10), Point2d(x=3, y=15), Point2d(x=7, y=12), Point2d(x=12, y=0), Point2d(x=15, y=10), Point2d(x=20, y=8), Point2d(x=24, y=0)]}, 'leetcode 2': {'in': [Building(left=0, height=3, right=2), Building(left=2, height=3, right=5)], 'out': [Point2d(x=0, y=3), Point2d(x=5, y=0)]}, 'Udi Manber': {'in': [Building(left=1, height=11, right=5), Building(left=2, height=6, right=7), Building(left=3, height=13, right=9), Building(left=12, height=7, right=16), Building(left=14, height=3, right=25), Building(left=19, height=18, right=22), Building(left=23, height=13, right=29), Building(left=24, height=4, right=28)], 'out': [Point2d(x=1, y=11), Point2d(x=3, y=13), Point2d(x=9, y=0), Point2d(x=12, y=7), Point2d(x=16, y=3), Point2d(x=19, y=18), Point2d(x=22, y=3), Point2d(x=23, y=13), Point2d(x=29, y=0)]}}\n"
     ]
    }
   ],
   "source": [
    "test_set = '''\n",
    "{\n",
    "\"consecutive\": {\n",
    "\"in\": [[0, 2, 1], [1, 3, 2], [2, 2, 3], [3, 2, 4]], \n",
    "\"out\": [[0, 2], [1, 3], [2, 2], [4, 0]]\n",
    "}, \n",
    "\"stairway to heaven\": {\n",
    "\"in\": [[1, 1, 5], [2, 2, 5], [3, 3, 5], [4, 4, 5]], \n",
    "\"out\": [[1, 1], [2, 2], [3, 3], [4, 4], [5, 0]]\n",
    "}, \n",
    "\"stairway from heaven\": {\n",
    "\"in\": [[1, 4, 2], [1, 3, 3], [1, 2, 4], [1, 1, 5]], \n",
    "\"out\": [[1, 4], [2, 3], [3, 2], [4, 1], [5, 0]]\n",
    "}, \n",
    "\"flat\": {\n",
    "\"in\": [[1, 1, 5], [2, 1, 6], [3, 1, 7], [4, 1, 8]], \n",
    "\"out\": [[1, 1], [8, 0]]\n",
    "}, \n",
    "\"tall\": {\n",
    "\"in\": [[1, 1, 2], [1, 3, 2], [1, 4, 2], [1, 2, 2]], \n",
    "\"out\": [[1, 4], [2, 0]]\n",
    "}, \n",
    "\"leetcode 1\": {\n",
    "\"in\": [[2, 10, 9], [3, 15, 7], [5, 12, 12], [15, 10, 20], [19, 8, 24]], \n",
    "\"out\": [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]\n",
    "}, \n",
    "\"leetcode 2\": {\n",
    "\"in\": [[0, 3, 2], [2, 3, 5]], \n",
    "\"out\": [[0, 3], [5, 0]]\n",
    "},\n",
    "\"Udi Manber\": {\n",
    "\"in\": [[1, 11, 5], [2, 6, 7], [3, 13, 9], [12, 7, 16], [14, 3, 25], [19, 18, 22], [23, 13, 29], [24, 4, 28]], \n",
    "\"out\": [[1, 11], [3, 13], [9, 0], [12, 7], [16, 3], [19, 18], [22, 3], [23, 13], [29, 0]]\n",
    "}\n",
    "}\n",
    "'''\n",
    "from json import loads\n",
    "test_set = loads(test_set)\n",
    "\n",
    "for v in test_set.values():\n",
    "    d = v[\"in\"]\n",
    "    s = v[\"out\"]\n",
    "    for i, b in enumerate(d):\n",
    "        d[i] = Building(*b)\n",
    "    for i, p in enumerate(s):\n",
    "        s[i] = Point2d(*p)\n",
    "        \n",
    "print(test_set)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "c10563f9",
   "metadata": {},
   "outputs": [],
   "source": [
    "def skyline_height(buildings, x):\n",
    "    h = 0\n",
    "    for b in buildings:\n",
    "        if b.left <= x < b.right:\n",
    "            h = max(h, b.height)\n",
    "    return h    "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dda06f39",
   "metadata": {},
   "source": [
    "Let us first present a simple quadratic time solution to the skyline problem"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "7fe0280b",
   "metadata": {},
   "outputs": [],
   "source": [
    "def add_point(points, p):\n",
    "    assert p.y >= 0\n",
    "    if points: \n",
    "        #assert points[-1].x <= p.x\n",
    "        if points[-1].x == p.x and points[-1].y < p.y:\n",
    "            points[-1] = p\n",
    "        elif points[-1].y != p.y:\n",
    "            points.append(p)\n",
    "    elif p.y > 0:\n",
    "        points.append(p)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "11617548",
   "metadata": {},
   "outputs": [],
   "source": [
    "def skyline_quadratic(buildings):\n",
    "    edges = [b.left for b in buildings] + [b.right for b in buildings]\n",
    "    edges.sort()\n",
    "    points = []\n",
    "    for x in edges:\n",
    "        add_point(points, Point2d(x, skyline_height(buildings, x)))\n",
    "    return points    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "e37d0a5f",
   "metadata": {},
   "outputs": [],
   "source": [
    "for test in test_set.values():\n",
    "    assert skyline_quadratic(test[\"in\"]) == test[\"out\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "8d7230b1",
   "metadata": {},
   "outputs": [],
   "source": [
    "from heapq import heappush, heappop\n",
    "\n",
    "def skyline_heapq(buildings):    \n",
    "    buildings = [Building(*b) for b in buildings]\n",
    "    buildings.sort(key=lambda b: b.left)\n",
    "    edges = [b.left for b in buildings] + [b.right for b in buildings]\n",
    "    edges.sort()\n",
    "    points = []\n",
    "    q = []\n",
    "    i = 0\n",
    "    for x in edges:\n",
    "        while i < len(buildings) and buildings[i].left <= x:\n",
    "            heappush(q, (- buildings[i].height, buildings[i].right))\n",
    "            i += 1\n",
    "        while q and q[0][1] <= x: heappop(q)\n",
    "        add_point(points, Point2d(x, - q[0][0] if q else 0))       \n",
    "    return points"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "9e9bd27f",
   "metadata": {},
   "outputs": [],
   "source": [
    "from heapq import heappush, heappop\n",
    "\n",
    "def skyline_height_heapq(buildings, *args):    \n",
    "    heights = []\n",
    "    q = []\n",
    "    i = 0\n",
    "    for x in args:\n",
    "        while i < len(buildings) and buildings[i].left <= x:\n",
    "            heappush(q, (- buildings[i].height, buildings[i].right))\n",
    "            i += 1\n",
    "        while q and q[0][1] <= x: heappop(q)\n",
    "        heights.append(- q[0][0] if q else 0)       \n",
    "    return heights\n",
    "\n",
    "def skyline_heapq_better(buildings):\n",
    "    buildings = [Building(*b) for b in buildings]\n",
    "    buildings.sort(key=lambda b: b.left)\n",
    "    edges = [b.left for b in buildings] + [b.right for b in buildings]\n",
    "    edges.sort()\n",
    "    points = []\n",
    "    for e, h in zip(edges, skyline_height_heapq(buildings, *edges)) :\n",
    "        add_point(points, Point2d(e, h))\n",
    "    return points"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "8027e33f",
   "metadata": {},
   "outputs": [],
   "source": [
    "for test in test_set.values():\n",
    "    assert skyline_heapq_better(test[\"in\"]) == test[\"out\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "999ffb20",
   "metadata": {},
   "outputs": [],
   "source": [
    "def merge_skylines(points1, points2):\n",
    "    dirty_points = []\n",
    "    i1 = len(points1) - 1\n",
    "    i2 = len(points2) - 1\n",
    "    while i1 >= 0 and i2 >= 0:\n",
    "        p1 = points1[i1]\n",
    "        p2 = points2[i2]\n",
    "        x = max(p1.x, p2.x)\n",
    "        dirty_points.append(Point2d(x, max(p1.y, p2.y)))\n",
    "        if p1.x == x: i1 -= 1\n",
    "        if p2.x == x: i2 -= 1  \n",
    "    points = points1[:i1 + 1] + points2[:i2 + 1]\n",
    "    for p in reversed(dirty_points):\n",
    "        add_point(points, p) \n",
    "    return points"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "8b7a8ab7",
   "metadata": {},
   "outputs": [],
   "source": [
    "def skyline_dc(buildings):\n",
    "    l = len(buildings)\n",
    "    if l == 1:\n",
    "        b ,= buildings\n",
    "        return [Point2d(b.left, b.height), Point2d(b.right, 0)]\n",
    "    return merge_skylines(skyline_dc(buildings[:l//2]), skyline_dc(buildings[l//2:]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "0789d2f1",
   "metadata": {},
   "outputs": [],
   "source": [
    "for test in test_set.values():\n",
    "    assert skyline_dc(test[\"in\"]) == test[\"out\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "03991455",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 5, 8]\n"
     ]
    }
   ],
   "source": [
    "def from_sorting_to_skyline(skyline, l):\n",
    "    l = list(l)\n",
    "    m = min(l) \n",
    "    M = max(l)    \n",
    "    buildings = [Building(x - m, x - m + 1, M - m + i) for i, x in enumerate(l, 1)]\n",
    "    points = skyline(buildings)\n",
    "    return [p.x + m for p in points[:len(l)]]\n",
    "\n",
    "print(from_sorting_to_skyline(skyline_quadratic, [5, 2, 3, 8, 1]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "e03b6091",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(1, 2, 3)\n"
     ]
    }
   ],
   "source": [
    "def f(*args):\n",
    "    print(args)\n",
    "    \n",
    "f(1, 2, 3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "15b574d9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
