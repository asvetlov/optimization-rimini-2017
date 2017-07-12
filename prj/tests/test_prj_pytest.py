import pytest


from prj import _pyappend
try:
    from prj import _append
except ImportError:
    _append = None


@pytest.fixture(params=[_append, _pyappend],
                ids=['Cython', 'Python'])
def append(request):
    return request.param


def test_append(append):
    lst = [1, 2]
    append(lst, 3, 2)
    assert [1, 2, 3, 3] == lst
