cdef extern from "Python.h":
    object PyUnicode_New(Py_ssize_t size, Py_UCS4 maxchar)
    void PyUnicode_WriteChar(object u, Py_ssize_t index, Py_UCS4 value)
    object PyUnicode_Substring(object u, Py_ssize_t start, Py_ssize_t end)


import string

def cyaddchar(str s):
    for ch in string.ascii_letters:
        s += ch
    return s


def cyaddchar2(str s):
    cdef Py_ssize_t ret_size = len(s) + len(string.ascii_letters)
    cdef object ret = PyUnicode_New(ret_size, 1114111)
    cdef Py_ssize_t idx = 0
    for ch in string.ascii_letters:
        PyUnicode_WriteChar(ret, idx, ch)
        idx += 1
    return s
