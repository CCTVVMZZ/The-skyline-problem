from collections import namedtuple


class Box(namedtuple("_RawBox", ["left", "height", "right"])):
    
    def __contains__(self, pair):
        x, y = pair
        return self.left <= x < self.right and y <= self.height

    def intersects(self, other):
        """

        >>> Box(1, 5, 3).intersects(Box(1, 5, 3))
        True
        
        >>> Box(1, 6, 4).intersects(Box(2, 5, 3))
        True
        
        >>> Box(1, 5, 3).intersects(Box(2, 6, 4))
        True
        
        >>> Box(2, 6, 4).intersects(Box(1, 5, 3))
        True
        
        >>> Box(1, 5, 3).intersects(Box(3, 6, 4))
        False

        >>> Box(3, 6, 4).intersects(Box(1, 5, 3))
        False
        
        """
        # two comparisons 
        if self.left <= other.left:
            return other.left < self.right
        return self.left < other.right


if __name__ == "__main__":
    import doctest
    doctest.testmod()


        
