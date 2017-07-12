def cysum(start, step, count):
    ret = start
    for i in range(count):
        ret += step
    return ret


def cysum2(float start, float step, int count):
    cdef float ret
    ret = start
    for i in range(count):
        ret += step
    return ret
