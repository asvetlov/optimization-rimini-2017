import timeit
import pyximport; pyximport.install()
from mod2 import cysum, cysum2

def pysum(start, step, count):
    ret = start
    for i in range(count):
        ret += step
    return ret


print('Python',
      timeit.timeit('pysum(0, 1, 100)', 'from __main__ import pysum'))
print('Cython', timeit.timeit('cysum(0, 1, 100)', 'from __main__ import cysum'))
print('Cython with types',
      timeit.timeit('cysum2(0, 1, 100)', 'from __main__ import cysum2'))
