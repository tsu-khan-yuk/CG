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


class Algorithms:
    word = {
        'S': [ 
            [Dot(20, 6), Dot(30, 16)], 
            [Dot(10, 16), Dot(20, 6)],
            [Dot(10, 16), Dot(30, 36)],
            [Dot(10, 36), Dot(20, 46)],
            [Dot(20, 46), Dot(30, 36)]
        ],
        'u1': [
            [Dot(35, 26), Dot(35, 46)],
            [Dot(35, 46), Dot(45, 46)],
            [Dot(45, 46), Dot(48, 44)],
            [Dot(48, 26), Dot(48, 46)]
        ],
        'h':  [
            [Dot(53, 6), Dot(53, 46)],
            [Dot(53, 26), Dot(63, 26)],
            [Dot(63, 26), Dot(66, 29)],
            [Dot(66, 29), Dot(66, 46)]
        ],
        'a': [
            [Dot(71, 26), Dot(71, 46)],
            [Dot(71, 26), Dot(84, 26)],
            [Dot(71, 46), Dot(81, 46)],
            [Dot(81, 46), Dot(84, 43)],
            [Dot(84, 26), Dot(84, 46)]
        ],
        'n': [
            [Dot(89, 26), Dot(89, 46)],
            [Dot(89, 29), Dot(97, 26)],
            [Dot(97, 26), Dot(99, 26)],
            [Dot(99, 26), Dot(102, 28)],
            [Dot(102, 29), Dot(102, 46)]
        ],
        'i': [
            [Dot(107, 26), Dot(107, 46)],
            [Dot(107, 23), Dot(107, 22)],
        ],
        'u2': [
            [Dot(112, 26), Dot(112, 46)],
            [Dot(112, 46), Dot(122, 46)],
            [Dot(122, 46), Dot(125, 44)],
            [Dot(125, 26), Dot(125, 46)],
        ],
        'k': [
            [Dot(130, 6), Dot(130, 46)],
            [Dot(130, 36), Dot(140, 26)],
            [Dot(130, 36), Dot(140, 46)],
        ]
    }

    def __init__(self):
        root = tk.Tk()
        root.title('Lab 1')
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg='black')
        self.canvas.pack()
        frame = tk.Frame(root, bg='black')
        frame.pack()

        dda = tk.Button(frame, text='\t\tDDA\t\t', command=self.algorithm_manger('DDA'))
        dda.grid(row=1, column=1)

        root.mainloop()

    def algorithm_manger(self, algorithm_name: str):
        def func():
            for letter in self.word.keys():
                for coords in self.word[letter]:
                    getattr(self, algorithm_name)(coords[0], coords[1])
        return func

    def draw(self, point: Dot):
        self.canvas.create_rectangle(
            PIXEL_SIZE * point.x,
            PIXEL_SIZE * point.y,
            PIXEL_SIZE * point.x + PIXEL_SIZE,
            PIXEL_SIZE * point.y + PIXEL_SIZE,
            fill="white",
            tag="word"
        )

    def DDA(self, dot_1: Dot, dot_2: Dot) -> None:

        condition = np.abs(dot_2.x - dot_1.x) >= np.abs(dot_2.y - dot_1.y)
        length = np.abs(dot_2.x - dot_1.x) if condition else np.abs(dot_2.y - dot_1.y)

        delta_x = (dot_2.x - dot_1.x) / length
        delta_y = (dot_2.y - dot_1.y) / length

        x = dot_1.x
        y = dot_1.y

        i = 0
        while i <= length:
            self.draw(Dot(round(x), round(y)))
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


    