class VanEmdeBoasTree:
    """
    Van Emde Boas Tree.
    """

    def __init__(self, bit_length):
        """
        Generates an empty veb-tree with the given range.
        """
        
        self.min = None
        self.max = None
        self.u = 1 << bit_length

        if bit_length == 1:
            self.summary = False
        else:
            self.lsb_size = bit_length >> 1
            msb_size = bit_length - self.lsb_size 
            self.lsb_mask = (1 << self.lsb_size) - 1
            self.summary = VanEmdeBoasTree(msb_size)
            self.clusters = [ VanEmdeBoasTree(self.lsb_size) for _ in range(1 << msb_size) ]
            

    def __bool__(self):
        """
        Non-empty veb-trees are truthy.
        """
        return self.min is not None
        # return self.max is not None
        
            
    def k_split(self, key):
        return key >> self.lsb_size, key & self.lsb_mask 
         

    def k_merge(self, hi, lo):
        return (hi << self.lsb_size) + lo

    
    def __contains__(self, key):
        """
        Checks whether key is present in self.
        """

        if not self:
            return False
        
        if key == self.min or key == self.max:
            return True

        if not self.summary:
            return False

        hi, lo = self.k_split(key)
        return lo in self.clusters[hi]


    def pred(self, key):
        """
        Returns the predecessor of key in self.
        """

        if not self:
            return None
        
        if key > self.max:
            return self.max
        
        if key <= self.min:
            return None
        
        if not self.summary:
            return self.min

        hi, lo = self.k_split(key)
        c = self.clusters[hi]

        if c and c.min < lo:
            return self.k_merge(hi, c.pred(lo))

        pred_hi = self.summary.pred(hi)
        if pred_hi is not None:
            return self.k_merge(pred_hi, self.clusters[pred_hi].max)

        return self.min 


    def succ(self, key):
        """
        Returns the successor of key in self.
        """
        
        if not self:
            return None
        
        if key < self.min:
            return self.min
        
        if key >= self.max:
            return None
        
        if not self.summary:
            return self.max

        hi, lo = self.k_split(key)
        c = self.clusters[hi]

        if c and c.max > lo:
            return self.k_merge(hi, c.succ(lo))

        succ_hi = self.summary.succ(hi)
        if succ_hi is not None:
            return self.k_merge(succ_hi, self.clusters[succ_hi].min)
        
        return self.max 


    def add(self, key):
        """
        Inserts key into self.
        """
        if not self:
            self.min = self.max = key
            return
        
        if key == self.min or key == self.max:
            return
        
        if self.min == self.max:
            if key < self.min:
                self.min = key
            elif key > self.max:
                self.max = key
            return

        if key < self.min:
            self.min, key = key, self.min
        elif key > self.max:
            self.max, key = key, self.max

        hi, lo = self.k_split(key)
        c = self.clusters[hi]

        if not c:
            self.summary.add(hi)

        c.add(lo)


    def discard(self, key):
        """
        Deletes key from self.
        """
        if not self or key < self.min or key > self.max:
            return

        if self.min == self.max:
            self.min = self.max = None
            return

        if not self.summary:
            if key == self.min:
                self.min = self.max
            elif key == self.max:
                self.max = self.min
            return
        
        if key == self.min:
            
            hi = self.summary.min
            c = self.clusters[hi]
            lo = c.min
            self.min = self.k_merge(hi, lo)

        elif key == self.max:

            hi = self.summary.max
            c = self.clusters[hi]
            lo = c.max
            self.max = self.k_merge(hi, lo)

        else:
            hi, lo = self.k_split(key)
            c = self.clusters[hi]

        c.discard(lo)

        if not c:
            self.summary.discard(hi)



    def __iter__(self):
        """
        Iterator over the elements in self.
        """
        key = self.min
        while key != None:
            yield key 
            key = self.succ(key)



