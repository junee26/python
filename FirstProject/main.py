from math import sqrt
def per_sqr(x):
    if x >= 0:
        sr = (sqrt(x))
        print(sr * sr);
        return (sr * sr) == x
    return False

print(per_sqr(4))
