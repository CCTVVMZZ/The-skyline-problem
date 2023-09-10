import unittest
from random import shuffle
from pred_succ_discard import PredSuccDiscard

class TestDiscardFirst(unittest.TestCase):

    PSD = PredSuccDiscard

    @classmethod
    def setUpClass(cls):
        
        cls.discarded = [0, 1, 2,
                          18,
                          30, 31, 32, 33,
                          60,
                          97, 98, 99]
        cls.remaining = [ i for i in range(100) if i not in set(cls.discarded) ]
        cls.discarded *= 2
        shuffle(cls.discarded)
    
    def setUp(self):
        
        self.psd = self.PSD(100)
        for i in self.discarded:
            self.psd.discard(i)

    def test_left(self):
        
        self.assertEqual(self.psd.pred(4), 3)
        
        self.assertIsNone(self.psd.pred(3))
        self.assertIsNone(self.psd.pred(2))
        self.assertIsNone(self.psd.pred(1))
        self.assertIsNone(self.psd.pred(0))
        self.assertIsNone(self.psd.pred(-1))
        self.assertIsNone(self.psd.pred(-2))
    
    def test_right(self):
        
        self.assertEqual(self.psd.succ(95), 96)
        
        self.assertIsNone(self.psd.succ(96))
        self.assertIsNone(self.psd.succ(97))
        self.assertIsNone(self.psd.succ(98))
        self.assertIsNone(self.psd.succ(99))
        self.assertIsNone(self.psd.succ(100))
        self.assertIsNone(self.psd.succ(101))

    def test_middle_succ(self):
        
        self.assertEqual(self.psd.succ(28), 29)
        
        self.assertEqual(self.psd.succ(29), 34)
        self.assertEqual(self.psd.succ(30), 34)
        self.assertEqual(self.psd.succ(31), 34)
        self.assertEqual(self.psd.succ(32), 34)
        self.assertEqual(self.psd.succ(33), 34)
        
        self.assertEqual(self.psd.succ(34), 35)
        
    def test_middle_pred(self):
        
        self.assertEqual(self.psd.pred(35), 34)
        
        self.assertEqual(self.psd.pred(34), 29)
        self.assertEqual(self.psd.pred(33), 29)
        self.assertEqual(self.psd.pred(32), 29)
        self.assertEqual(self.psd.pred(31), 29)
        self.assertEqual(self.psd.pred(30), 29)
        
        self.assertEqual(self.psd.pred(29), 28)

    def test_iter(self):
        
        self.assertListEqual(list(self.psd), self.remaining)

    def test_contains(self):
        self.assertListEqual([ i for i in range(- 2, 102) if i in self.psd ],
                             self.remaining)

        
def pred(s, i):
    l = [ j for j in s if j < i ]
    return max(l) if l else None
    
def succ(s, i):
    l = [ j for j in s if j > i ]
    return min(l) if l else None


#class TestPredSuccDiscardIntertwined(unittest.TestCase):

#     # def setUp(self):
#     #     n = 200
#     #     self.s = list(range(n))
#     #     self.l = 
#     #     self.

#     def test_succ_full_to_empty(self):
#         n = 150
#         psd = PredSuccDiscard(n)
        
#         l = list(range(n))
#         s = set(l)
#         shuffle(l)
#         for i in l:
#             for j in range(- 2, n + 2):
# #                print(i, j, len(s))
#                 self.assertEqual(list(psd), sorted(list(s)))
#                 self.assertEqual(psd.pred(j), pred(s, j))
#                 self.assertEqual(psd.succ(j), succ(s, j))
#             psd.discard(i)
#             s.discard(i)

#         self.assertEqual(len(s), 0)
        
            
            
            

if __name__ == '__main__':
    unittest.main()
