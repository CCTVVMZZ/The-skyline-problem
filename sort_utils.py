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

            
def counting_sort(elts, /, *, key = lambda x: x):

    elts = tuple(elts)
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
    for e in elts:
        k = key(e)
        cts[k] -= 1
        res[cts[k]] = e

    return res
