from unittest import TestCase
from prj import _pyappend
try:
    from prj import _append
except ImportError:
    _append = None



class BasetTestMixin:
    def func(self, *args):
        raise NotImplementedError

    def test_append(self):
        lst = [1, 2]
        self.func(lst, 3, 2)
        self.assertEqual([1, 2, 3, 3], lst)


class TestPython(TestCase, BasetTestMixin):
    def func(self, *args):
        _pyappend(*args)



if _append is not None:
    class TestCython(TestCase, BasetTestMixin):
        def func(self, *args):
            _append(*args)
