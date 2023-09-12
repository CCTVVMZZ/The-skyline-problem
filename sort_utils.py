def merge_iterables(iterable1, iterable2, /, *, key = lambda x: x):
    """
    >>> list(merge_iterables([1, 1, 1], [2, 2, 2, 2], key = lambda x: 0))
    [1, 1, 1, 2, 2, 2, 2]
    """
    # The function is not symmetric in it1 and it2 and it must NOT be
    # in order to ensure the stability of the derived merge sort algorithm
    
    it1 = iter(iterable1)
    it2 = iter(iterable2)
    try:
        x1 = next(it1)
    except StopIteration:
        yield from it2
        return
    k1 = key(x1)
    while True:
        try:
            x2 = next(it2)
        except StopIteration:
            yield x1
            yield from it1
            return
        k2 = key(x2)
        while k1 <= k2:
            yield x1
            try:
                x1 = next(it1)
            except StopIteration:
                yield x2
                yield from it2
                return
            k1 = key(x1)
        yield x2
        

def merge_sort(elts, /, *,  key = lambda x: x): # useless 
    elts = list(elts)
    n = len(elts)
    if n <= 1:
        return elts
    n //= 2
    return merge_iterables(merge_sort(elts[:n], key = key), merge_sort(elts[n:], key = key), key = key)

            
def counting_sort(iterable, /, *, key = lambda x: x):

    elts = tuple(iterable)
    if not elts:
        return []    
    u = 1 + max(key(e) for e in elts)
    cts = [ 0 ] * u

    for e in elts:
        cts[key(e)] += 1

    for k in range(1, u):
        cts[k] += cts[k - 1]

    assert cts[u - 1] == len(elts)

    res = [ None ] * len(elts)
    for e in reversed(elts):
        k = key(e)
        cts[k] -= 1
        res[cts[k]] = e

    return res
