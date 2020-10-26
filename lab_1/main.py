"""
TODO:
    --> add logging
"""
import tkinter as tk
import numpy as np
import warnings
import time
PIXEL_SIZE = 5
HEIGHT = 500
WIDTH = 800


warnings.simplefilter('ignore', DeprecationWarning)


def time_counter(func):
    def wrapper(*args, **kwargs):
        start_time = time.clock()
        val = func(*args, **kwargs)
        print(str(time.clock() - start_time))
        return val
    return wrapper


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


class Painter:
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
        'h': [
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

        dda_button = tk.Button(frame, text='\tDDA\t', command=self.algorithm_manager('DDA'))
        dda_button.grid(row=1, column=1)

        bresenham_button = tk.Button(frame, text='\tBresenham\t', command=self.algorithm_manager('Bresenham'))
        bresenham_button.grid(row=1, column=2)

        circle_bresenham_button = tk.Button(frame, text='\tCircle Bresenham\t', command=self.algorithm_manager('cycle_Bresenham'))
        circle_bresenham_button.grid(row=1, column=3)

        wu_button = tk.Button(frame, text='\tWu\t', command=self.algorithm_manager('Wu'))
        wu_button.grid(row=1, column=4)

        clear_button = tk.Button(frame, text='\tClear\t', command=self.clean)
        clear_button.grid(row=1, column=5)

        root.mainloop()

    def algorithm_manager(self, algorithm_name: str):
        if algorithm_name == 'cycle_Bresenham':
            return lambda name=algorithm_name: getattr(self, algorithm_name)(Dot(85, 60), 15)
        else:
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

    def clean(self):
        self.canvas.delete('word')

    @time_counter
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
        print('DDA:')

    @time_counter
    def cycle_Bresenham(self, center: Dot, radius: int):
        x = 0
        y = radius
        delta = 1 - 2 * radius
        error = 0
        dots = []
        while (y >= 0):
            dots.append((center.x + x, center.y + y))
            dots.append((center.x + x, center.y - y))
            dots.append((center.x - x, center.y + y))
            dots.append((center.x - x, center.y - y))
            error = 2 * (delta + y) - 1
            if (delta < 0) and (error <= 0):
                x += 1
                delta += 2 * x + 1
                continue
            error = 2 * (delta - x) - 1
            if delta > 0 and error > 0:
                y -= 1
                delta += 1 - 2 * y
                continue
            x += 1
            delta += 2 * (x - y)
            y -= 1
        print('cycle_Bresenham:')
        for coord in dots:
            self.draw(Dot(coord[0], coord[1]))

    @time_counter
    def Bresenham(self, dot_1: Dot, dot_2: Dot):
        delta_x = dot_2.x - dot_1.x
        delta_y = dot_2.y - dot_1.y
        # Determine how steep the line is
        is_steep = np.abs(delta_y) > np.abs(delta_x)
        # Rotate line
        if is_steep:
            dot_1.x, dot_1.y = dot_1.y, dot_1.x
            dot_2.x, dot_2.y = dot_2.y, dot_2.x
        # Swap start and end points if necessary
        if dot_1.x > dot_2.x:
            dot_1.x, dot_2.x = dot_2.x, dot_1.x
            dot_1.y, dot_2.y = dot_2.y, dot_1.y
        
        # Recalculate differentials
        delta_x = dot_2.x - dot_1.x
        delta_y = dot_2.y - dot_1.y
        
        # Calculate error
        error = int(delta_x / 2.0)
        ystep = 1 if dot_1.y < dot_2.y else -1
        
        # Iterate over bounding box generating points between start and end
        y = dot_1.y
        for x in range(dot_1.x, dot_2.x + 1):
            self.draw(Dot(y, x) if is_steep else Dot(x, y))
            error -= np.abs(delta_y)
            if error < 0:
                y += ystep
                error += delta_x
        print('Bresenham:')

    @time_counter
    def Wu(self, dot_1: Dot, dot_2: Dot):

        _fpart = lambda x: x - int(x)
        _rfpart = lambda x: 1 - _fpart(x)
        
        dots = []
        delta_x, delta_y = dot_2.x - dot_1.x, dot_2.y - dot_1.y
        x, y = dot_1.x, dot_1.y
        
        if delta_y == 0:
            dots.append([round(x), round(dot_1.y)])
            while np.abs(x) < np.abs(dot_2.x):
                x += 1
                dots.append([round(x), round(dot_1.y)])
        
        elif delta_x == 0:
            dots.append([round(dot_1.x), round(y)])
            while np.abs(y) < np.abs(dot_2.y):
                y += 1
                dots.append([round(dot_1.x), round(y)])
        else:
            grad = delta_y / delta_x
            intery = dot_1.y + _rfpart(dot_1.x) * grad
            
            def draw_endpoint(x, y):
                xend = round(x)
                yend = y + grad * (xend - x)
                px, py = int(xend), int(yend)
                dots.append([px, py])
                dots.append([px, py + 1])
                return px
            
            xstart = draw_endpoint(dot_1.x, dot_1.y)
            xend = draw_endpoint(dot_2.x, dot_2.y)
            
            for x in range(xstart, xend):
                y = int(intery)
                dots.append([x, y])
                dots.append([x, y + 1])
                intery += grad
        print('Wu:')
        for coord in dots:
            self.draw(Dot(coord[0], coord[1]))


if __name__ == '__main__':
    val = Painter()


    