import functools
@functools.lru_cache(maxsize=None)
def fiboncci(n):
    if n<2:
        return n
    return fiboncci(n-1)+fiboncci(n-2)
print(fiboncci(20))