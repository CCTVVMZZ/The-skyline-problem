def infinity_factory(cls = object):

    class Infinity(cls):
        
        def __init__(self, negative):
            self._negative = negative

        def __lt__(self, other):
            return (self is not other) and self._negative 

        def __le__(self, other):
            return (self is other) or self._negative

        def __gt__(self, other):
            return not self.__le__(other)

        def __ge__(self, other):
            return not self.__lt__(other)

    return Infinity(True), Infinity(False)

if __name__ == "__main__":

    import __main__
    print("Testing", __main__.__file__)
    
    
    class OldClass:
        
        def __lt__(self, other):
            return False
        
        def __le__(self, other):
            return False

        def __gt__(self, other):
            return False
        
        def __ge__(self, other):
            return False

        
    n, p = infinity_factory()

    assert n == n
    assert p == p
    
    assert n != p
    assert p != n
    
    assert n < p
    assert p > n
    
    assert n <= n
    assert p <= p
    
    assert n >= n
    assert p >= p

    old = OldClass()
    assert not isinstance(old, type(n))
    assert not isinstance(old, type(p))

    n_new, p_new = infinity_factory()
    
    for x in [42, 4.2, "foo", lambda x: x / 2, object(), old, n_new, p_new]:
        assert n < x
        assert n <= x
        assert p > x
        assert p >= x        
        
    # so far, so good !
    
    
    assert not (old > n)
    assert not (old < p)
    assert not (old >= n)
    assert not (old <= p)
    
    n_new_new, p_new_new = infinity_factory(type(n))
    assert isinstance(n_new_new, type(n))
    assert isinstance(p_new_new, type(p))

    assert not (n < n_new_new)
    assert not (p > p_new_new)

    # Oooops !
