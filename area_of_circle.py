# Trying out the area of a circle the way it's done
# to explain calculus in 3blue2brown's video 1 of the
# calculus series.

import math

import numpy as np


def normal_circle_area(r):
    return math.pi * r**2


def contrived_circle_area(r):
    area = 0
    dr = 0.00001  # the smaller the value, the closer the approximation
    for i in np.arange(0, r, dr):
        width = dr  # Just to make the naming logical
        height = 2 * i * math.pi
        area = area + (width * height)
    return area


if __name__ == '__main__':
    r = 3
    print("Normal area of circle: ", normal_circle_area(r))
    print("Contrived area of circle: ", contrived_circle_area(r))
