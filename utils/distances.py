def manhattan(a, b):
    a = (1, 1)
    b = (4, 5)

    d_x = b[0] - a[0]
    d_y = b[1] - a[1]

    distance = d_x + d_y
    return distance 