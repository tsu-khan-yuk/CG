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
	

class Ink:
	dots = list()
	
	def __init__(self):
		root = tk.Tk()
		root.title('Lab 2')
		self.canvas = tk.Canvas(root, width=1200, height=500, bg='black')
		self.canvas.pack()
		frame = tk.Frame(root, bg='black')
		frame.pack()
		
		self.dots = [
			Dot(82, 40),
			Dot(100, 25),
			Dot(120, 60),
			Dot(140, 40)
		]
		self.draw_raster()
		
		root.mainloop()
	
	def __draw(self, point: Dot):
		self.canvas.create_rectangle(
			PIXEL_SIZE * point.x,
			PIXEL_SIZE * point.y,
			PIXEL_SIZE * point.x + PIXEL_SIZE,
			PIXEL_SIZE * point.y + PIXEL_SIZE,
			fill="white",
			tag="bezier"
		)
		
	def draw_raster(self):
		for dot_counter in range(len(self.dots) - 1):
			dot_1 = self.dots[dot_counter]
			dot_2 = self.dots[dot_counter + 1]
			
			condition = np.abs(dot_2.x - dot_1.x) >= np.abs(dot_2.y - dot_1.y)
			length = np.abs(dot_2.x - dot_1.x) if condition else np.abs(dot_2.y - dot_1.y)
			
			delta_x = (dot_2.x - dot_1.x) / length
			delta_y = (dot_2.y - dot_1.y) / length
			
			x = dot_1.x
			y = dot_1.y
			
			for i in range(length + 1):
				self.__draw(Dot(round(x), round(y)))
				x += delta_x
				y += delta_y
		
		
if __name__ == '__main__':
	Ink()