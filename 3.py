import timeit
import pyximport; pyximport.install()
from mod3 import cyappend, cyappend2

def pyappend(lst, item, count):
    for i in range(count):
        lst.append(item)


print('Python',
      timeit.timeit('pyappend([], 1, 100)', 'from __main__ import pyappend'))
print('Cython',
      timeit.timeit('cyappend([], 1, 100)', 'from __main__ import cyappend'))
print('Cython with types',
      timeit.timeit('cyappend2([], 1, 100)', 'from __main__ import cyappend2'))
