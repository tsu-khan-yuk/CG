"""
    # TODO:
        -> add graphic function
"""
import tkinter as tk
import numpy as np
PIXEL_SIZE = 5


class Dot:
    x = None
    y = None

    def __init__(self, x, y) -> None:
        if isinstance(x, (int, float)) and isinstance(y, (int, float)):
            self.x = x
            self.y = y
        else:
            raise TypeError('Invalid "x" or "y" type')

    def deepcopy(self):
        return Dot(self.x, self.y)

    def __str__(self) -> str:
        return '({}, {})'.format(self.x, self.y)


class BezierCalculator:
    __coordinates = list()

    def __init__(self):

        root = tk.Tk()
        root.title('Lab 2')
        self.canvas = tk.Canvas(root, width=800, height=500, bg='black')
        self.canvas.pack()
        frame = tk.Frame(root, bg='black')
        frame.pack()

        test_dot_list = [
            Dot(2, 20),
            Dot(20, 5),
            Dot(40, 40),
            Dot(70, 20)
        ]

        self.curve_calculating(test_dot_list)

        root.mainloop()

    def clean(self):
        self.canvas.delete('bezier')

    def draw(self, point: Dot):
        self.canvas.create_rectangle(
            PIXEL_SIZE * point.x,
            PIXEL_SIZE * point.y,
            PIXEL_SIZE * point.x + PIXEL_SIZE,
            PIXEL_SIZE * point.y + PIXEL_SIZE,
            fill="white",
            tag="bezier"
        )

    @staticmethod
    def x_t(t, p: Dot):
        return p[0].x*((1 - t)**3) + 3*t*p[1].x*((1 - t)**2) + 3*(t**2)*p[2].x*(1 - t) + (t**3)*p[3].x

    @staticmethod
    def y_t(t, p: Dot):
        return p[0].y*((1 - t)**3) + 3*t*p[1].y*((1 - t)**2) + 3*(t**2)*p[2].y*(1 - t) + (t**3)*p[3].y

    def curve_calculating(self, dots: list):
        delta_t = 0
        while delta_t <= 1:
            x = self.x_t(delta_t, dots)
            y = self.y_t(delta_t, dots)
            print(round(x, 2), round(y, 2))
            self.draw(Dot(round(x, 2), round(y, 2)))
            delta_t += 0.01


if __name__ == '__main__':
    var = BezierCalculator()
