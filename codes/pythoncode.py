import math
def hix(x):
    if x > 0:
        return x
    else:
        return 0

def trans1(x1, x2, n, s1, s2, lock):
# 1.	(A1,B1) -> (A1,B1)
    if lock == 1:
        dt = 22 * (math.floor(x1 / 2) + math.floor(x2 / 2))
        dw = math.floor(x1 / 2) * n + math.floor(x2 / 2) * (150 - n)
        return dt, dw, lock
    else:
        return 0, 0, lock