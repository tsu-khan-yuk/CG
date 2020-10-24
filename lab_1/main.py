import tkinter as tk
import numpy as np
import time
PIXEL_SIZE = 5
HEIGHT = 500
WIDTH = 800


class Dot:
    x = None
    y = None

    def __init__(self, x, y) -> None:
        if isinstance(x, (int, float)) and isinstance(y, (int, float)):
            self.x = x
            self.y = y
        else:
            raise TypeError('Invalid "x" or "y" type')

    def __str__(self) -> str:
        return '({}, {})'.format(self.x, self.y)


class Line:
    start = None
    end = None

    def __init__(self, start: Dot, end: Dot) -> None:
        if isinstance(start, Dot) and isinstance(end, Dot):
            self.start = start
            self.end = end
        else:
            raise TypeError('Invalid "start" or "end" type')

    def __str__(self):
        return '[{}, {}]'.format(str(self.start), str(self.end))


class Algorithms:
    base = {
        'S': [
            # (Dot(), Dot()), 
            [Dot(20, 5), Dot(10, 10)], 
            [Dot(10, 10), Dot(30, 30)],
            # (Dot(), Dot()),
            # (Dot(), Dot()) 
        ],
        'u': None,
        'k': None,
        'h': None,
        'a': None,
        'n': None,
        'i': None,
        'u': None,
        'k': None
    }

    def __init__(self):
        root = tk.Tk()
        root.title('Lab 1')
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg='black')
        self.canvas.pack()
        frame = tk.Frame(root, bg='black')
        frame.pack()

        dda = tk.Button(frame, text='\t\tDDA\t\t', command=self.command_manager('DDA'))
        dda.grid(row=1, column=1)

        root.mainloop()

    def command_manager(self, cmd_name: str):
        if cmd_name == 'DDA':
            def func():
                for i in self.base['S']:
                    self.DDA(i[0], i[1])
            return func

    def draw(self, point: Dot):
        self.canvas.create_rectangle(
            PIXEL_SIZE * point.x,
            PIXEL_SIZE * point.y,
            PIXEL_SIZE * point.x + PIXEL_SIZE,
            PIXEL_SIZE * point.y + PIXEL_SIZE,
            fill="white",
            tag="base"
        )

    def DDA(self, dot_1: Dot, dot_2: Dot) -> None:

        if np.abs(dot_2.x - dot_1.x) >= np.abs(dot_2.y - dot_1.y):
            length = np.abs(dot_2.x - dot_1.x)
        else:
            length = np.abs(dot_2.y - dot_1.y)

        delta_x = (dot_2.x - dot_1.x) / length
        delta_y = (dot_2.y - dot_1.y) / length

        x = dot_1.x + 0.5*np.sign(delta_x)
        y = dot_2.y + 0.5*np.sign(delta_y)

        i = 0
        while i <= length:
            self.draw(Dot(x, y))
            x += delta_x
            y += delta_y
            i += 1

        return None

    def cycle_Bresenham(self, dot_1: Dot, dot_2: Dot):
        pass

    def Bresenham(self, dot_1: Dot, dot_2: Dot):
        pass

    def Wu(self, dot_1: Dot, dot_2: Dot):
        pass


if __name__ == '__main__':
    val = Algorithms()


    