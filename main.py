"""This function return area from triangle"""


def area_of_triangle(a, h):
    if a <= 0 or h <= 0:
        raise ValueError("Wrong value")
    return 0.5 * a * h


def area_of_circle(r):
    if r <= 0:
        raise ValueError("Wrong value")
    return r ** 2 * 3.14


def area_of_rectangle(w, h):
    if w <= 0 or h <= 0:
        ValueError("Wrong value")
    return w * h


class Figure:
    def __init__(self, name, parm):
        self.figure = name
        self.parm = parm

    def get_area(self):
        if self.figure == "triangle":
            return area_of_triangle(self.parm[0], self.parm[1])
        elif self.figure == "circle":
            return area_of_circle(self.parm[0])
        elif self.figure == "rectangle":
            return area_of_rectangle(self.parm[0], self.parm[1])


n, m = map(int, input("Введите числа для подсчета площади: ").split())
print(area_of_triangle(n, m))
