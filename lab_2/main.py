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

        self.curve_calculating(Dot(0, 0), Dot(10, 15), Dot(60, 40), Dot(90, 50))

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

    def curve_calculating(self, p1: Dot, p2: Dot, p3: Dot, p4: Dot):
        x_t = lambda t: p1.x*((1 - t)**3) + 3*t*p2.x*((1 - t)**2) + 3*(t**2)*p3.x*(1 - t) + (t**3)*p4.x
        y_t = lambda t: p1.y*((1 - t)**3) + 3*t*p2.y*((1 - t)**2) + 3*(t**2)*p3.y*(1 - t) + (t**3)*p4.y
        delta_t = 0
        while delta_t <= 2:
            x = x_t(delta_t)
            y = y_t(delta_t)
            print(round(x, 2), round(y, 2))
            self.draw(Dot(round(x, 2), round(y, 2)))
            delta_t += 0.09


if __name__ == '__main__':
    var = BezierCalculator()
