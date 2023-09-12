from random import shuffle
from pred_succ_discard import PredSuccDiscard as PSD
from pred_succ_add_discard_bisect import PredSuccAddDiscard as PSAD

full = list(range(100))

discarded = [0, 1, 2,
             18,
             30, 31, 32, 33,
             60,
             97, 98, 99,
             ]

remaining = [ i for i in full if i not in set(discarded) ]
discarded *= 2

def init():
    global psd
    global psad
    global discarded
    psd = PSD(100)
    psad = PSAD(range(100))
    
    shuffle(full)
    shuffle(discarded)
    
    for i in discarded:
        psd.discard(i)
        psad.discard(i)
    

init()

for i in full:
    assert psd.pred(i) == psad.pred(i)
    
init()

for i in full:
    assert psd.succ(i) == psad.succ(i)

init()

for i in full:
    assert psd.pred(i) == psad.pred(i)
    assert psd.succ(i) == psad.succ(i)

init()

assert list(psd) == remaining


    # def test_contains(self):
    #     self.assertListEqual([ i for i in range(- 2, 102) if i in self.psd ],
    #                          self.remaining)

        
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
        
            
            
            

