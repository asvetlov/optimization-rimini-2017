import string
import timeit
import pyximport; pyximport.install()
from mod4 import cyaddchar, cyaddchar2


def pyaddchar(s):
    for ch in string.ascii_letters:
        s += ch


print('Python',
      timeit.timeit('pyaddchar("")', 'from __main__ import pyaddchar'))
print('Cython',
      timeit.timeit('cyaddchar("")', 'from __main__ import cyaddchar'))
print('Cython with writechar',
      timeit.timeit('cyaddchar2("")', 'from __main__ import cyaddchar2'))
