"""This function return area from triangle"""


def area_of_triangle(a, h):
    if a <= 0 or h <= 0:
        raise ValueError("Wrong value")
    return 0.5 * a * h


def area_of_circle(r):
    return r**2*3.14


n, m = map(int, input("Введите числа для подсчета площади: ").split())
print(area_of_triangle(n, m))
