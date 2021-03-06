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

    def __add__(self, obj):
        self.x += obj.x
        self.y += obj.y
        return self

    def __sub__(self, obj):
        self.x += obj.x
        self.y += obj.y
        return self

    def deepcopy(self):
        return Dot(self.x, self.y)

    def __str__(self) -> str:
        return '({}, {})'.format(self.x, self.y)


class BezierCalculator:
    dots = list()
    width = int()
    height = int()
    scale = 1
    first_x = None
    first_y = None
    x_flag = True
    y_flag = True

    def __init__(self):

        root = tk.Tk()
        root.title('Lab 2')
        self.canvas = tk.Canvas(root, width=1200, height=500, bg='black')
        self.canvas.pack()
        frame = tk.Frame(root, bg='black')
        frame.pack()

        test_dot_list = [
            Dot(82, 40),
            Dot(100, 25),
            Dot(120, 60),
            Dot(140, 40)
        ]

        self.curve_calculating(test_dot_list)
        self.draw_rastring()

        # //////////////////////////////////////////////// SHIFTING //////////////////////////////////////////////////////
        up_button = tk.Button(frame, text='\t\tup\t\t', command=self.button_manager('up'))
        up_button.grid(row=1, column=0)

        down_button = tk.Button(frame, text='\t\tdown\t\t', command=self.button_manager('down'))
        down_button.grid(row=1, column=1)

        right_button = tk.Button(frame, text='\t\tright\t\t', command=self.button_manager('right'))
        right_button.grid(row=1, column=2)

        left_button = tk.Button(frame, text='\t\tleft\t\t', command=self.button_manager('left'))
        left_button.grid(row=1, column=3)

        #//////////////////////////////////////////////// SCALING ///////////////////////////////////////////////////////
        x1_button = tk.Button(frame, text='\t\t1x\t\t', command=self.button_manager('1x'))
        x1_button.grid(row=2, column=0)

        x2_button = tk.Button(frame, text='\t\t2x\t\t', command=self.button_manager('2x'))
        x2_button.grid(row=2, column=1)

        #//////////////////////////////////////////////// MIRRORING ///////////////////////////////////////////////////////
        x_mirroring_button = tk.Button(frame, text='\t\tmirroring X\t\t', command=self.button_manager('mirroringX'))
        x_mirroring_button.grid(row=2, column=2)

        y_mirroring_button = tk.Button(frame, text='\t\tmirroring Y\t\t', command=self.button_manager('mirroringY'))
        y_mirroring_button.grid(row=2, column=3)

        #//////////////////////////////////////////////// ANGLE /////////////////////////////////////////////////////////
        turn_clockwise_button = tk.Button(frame, text='\t\tturn clockwise\t\t', command=self.button_manager('forward'))
        turn_clockwise_button.grid(row=3, column=2)

        root.mainloop()

    def button_manager(self, button_name: str):
        if button_name in {'up', 'down', 'left', 'right'}:
            return lambda name=button_name: getattr(self, 'shifting_function')(name)
        elif button_name in {'1x', '2x'}:
            return lambda zoom=button_name: getattr(self, 'scaling_function')(zoom)
        elif 'mirroring' in button_name:
            return lambda axis=button_name: getattr(self, 'mirroring_function')(axis)
        elif button_name == 'forward':
            return lambda angle=45: getattr(self, 'angle_function')(angle)

    def shifting_function(self, cmd: str):
        self.clean()
        if cmd == 'up':
            dot_delta = Dot(0, -1)
        elif cmd == 'down':
            dot_delta = Dot(0, 1)
        elif cmd == 'left':
            dot_delta = Dot(-1, 0)
        elif cmd == 'right':
            dot_delta = Dot(1, 0)
        for i in range(len(self.dots)):
            self.dots[i] += dot_delta
        self.draw_rastring()

    def scaling_function(self, zoom):
        self.clean()
        if '1' in zoom:
            self.scale = 1
        elif '2' in zoom:
            self.scale = 2
        self.draw_rastring()

    def mirroring_function(self, axis):
        self.clean()
        length = len(self.dots) - 1
        if 'X' in axis:
            axis_delta = self.height if self.y_flag else -(self.height)
            self.y_flag = not self.y_flag
            for i in range(round(length/2)):
                self.dots[i].y += axis_delta
                self.dots[length - i].y += axis_delta
                self.dots[i].y, self.dots[length - i].y = self.dots[length - i].y, self.dots[i].y
        elif 'Y' in axis:
            axis_delta = self.width if self.x_flag else -(self.width)
            self.x_flag = not self.x_flag
            for i in range(round(length/2)):
                self.dots[i].x += axis_delta
                self.dots[length - i].x += axis_delta
                self.dots[i].x, self.dots[length - i].x = self.dots[length - i].x, self.dots[i].x
        self.draw_rastring()

    def angle_function(self, angle):
        self.clean()
        angle *= (np.pi / 180.0)
        buffer = list()
        x_shifting = (self.first_x + self.width/2)
        y_shifting = (self.first_y + self.height/2)

        for dot in self.dots:
            x = dot.x - x_shifting
            y = dot.y - y_shifting
            buffer.append(Dot(
                x=(x * np.cos(angle) - y * np.sin(angle)) + x_shifting,
                y=(x * np.sin(angle) + y * np.cos(angle)) + y_shifting
            ))

        self.dots = buffer
        self.draw_rastring()

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

    def curve_calculating(self, points: list):
        delta_t = 0
        while delta_t <= 1:
            x = self.x_t(delta_t, points)
            y = self.y_t(delta_t, points)
            # self.draw(Dot(round(x, 2), round(y, 2)))
            self.dots.append(Dot(round(x, 2), round(y, 2)))
            delta_t += 0.01
        x_list = sorted([i.x for i in points])
        y_list = sorted([i.y for i in points])
        self.first_x = x_list[0]
        self.first_y = y_list[0]
        self.width = x_list[-1] - x_list[0]
        self.height = y_list[-1] - y_list[0]

    def draw_rastring(self):
        j = 0
        while j < len(self.dots) - 1:
            dot_1 = self.dots[j]
            dot_2 = self.dots[j + 1]

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
            j += 1
        if self.scale == 2:
            self.canvas.scale('bezier', 0, 0, self.scale, self.scale)

if __name__ == '__main__':
    var = BezierCalculator()
