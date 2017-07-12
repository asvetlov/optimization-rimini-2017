try:
    from ._mod import _append
except ImportError:
    _append = None

def _pyappend(lst, item, count):
    for i in range(count):
        lst.append(item)


if _append is not None:
    append = _append
else:
    append = _pyappend
