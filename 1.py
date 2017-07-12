import timeit
import pyximport; pyximport.install()
from mod1 import cy, cy2

def py(a, b):
    return a + b


print('Python', timeit.timeit('py(1, 2)', 'from __main__ import py'))
print('Cython', timeit.timeit('cy(1, 2)', 'from __main__ import cy'))
print('Cython with types', timeit.timeit('cy2(1, 2)',
                                         'from __main__ import cy2'))
