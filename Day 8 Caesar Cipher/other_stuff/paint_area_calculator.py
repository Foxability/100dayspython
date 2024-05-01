import math

def paint_calc(height, width, cover):
    square_meters = height * width
    cans = math.ceil(square_meters / cover)
    print(cans)


test_h = int(input())
test_w = int(input())
coverage = 5


paint_calc(height=test_h, width=test_w, cover=coverage)
    