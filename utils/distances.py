def manhattan(a, b):
    d_x = abs(b[0] - a[0])
    d_y = abs(b[1] - a[1])
    return d_x + d_y
def euclidean(a, b):
    return minkowski(a, b, 2)

def minkowski(a, b, p):
    d_x = b[0] - a[0]
    d_y = b[1] - a[1]

    distance = (d_x**p + d_y**p)**(1/p)
    return distance