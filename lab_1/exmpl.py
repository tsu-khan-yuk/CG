# Import all definitions from tkinter

# from tkinter import *
import tkinter as tk
import time

PIXEL_SIZE = 5
HEIGHT = 500
WIDTH = 800


class RasterizationAlgorithms:
	surname = {
		"B": [[(10, 10), (10, 30)], [(10, 30), (22, 30)], [(22, 20), (22, 30)], [(10, 20), (22, 20)],
			  [(20, 10), (20, 20)], [(10, 10), (20, 10)]],
		"r": [[(30, 20), (30, 30)], [(30, 22), (38, 20)]],
		"y": [[(46, 20), (46, 30)], [(46, 30), (54, 30)], [(54, 20), (54, 45)], [(46, 45), (54, 45)]],
		"k": [[(62, 10), (62, 30)], [(62, 24), (70, 20)], [(62, 24), (70, 30)]],
		"a1": [[(78, 30), (82, 20)], [(82, 20), (86, 30)], [(80, 25), (84, 25)]],
		"l": [[(94, 10), (94, 30)], [(94, 30), (102, 30)]],
		"o": [[(114, 25), (4, 0)]],
		"v": [[(126, 20), (130, 30)], [(130, 30), (134, 20)]],
		"a2": [[(142, 30), (146, 20)], [(146, 20), (150, 30)], [(144, 25), (148, 25)]]
	}
	
	def DDA(self, x1, y1, x2, y2):
		t1 = time.clock()
		dx = abs(x2 - x1)
		dy = abs(y2 - y1)
		steps = dx if dx >= dy else dy
		dx = (x2 - x1) / steps
		dy = (y2 - y1) / steps
		
		x, y = x1, y1
		points = [[x, y], [x2, y2]]
		for i in range(steps - 1):
			x += dx
			y += dy
			points.append([round(x), round(y)])
		self.draw(points)
		t2 = time.clock()
		print("DDA:")
		print(t2 - t1)
	
	def assymetric_DDA(self, x1, y1, x2, y2):
		t1 = time.clock()
		dx = x2 - x1
		dy = y2 - y1
		points = [(x1, y1)]
		while (x1 < x2):
			x1 = x1 + 1.0
			y1 = y1 + dy / dx
			points.append([x1, y1])
		self.draw(points)
		
		dx = x2 - x1
		dy = y2 - y1
		x, y = x1, y1
		if dx and dy:
			if abs(dx) <= abs(dy):
				dy /= dx
				dx = 1.0
			else:
				dx /= dy
				dy = 1.0
			
			while abs(x) <= abs(x2):
				x += dx
				y += dy
				points.append([round(x), round(y)])
		
		elif dx:
			while abs(x) <= abs(x2):
				x += 1
				points.append([round(x), round(y1)])
		
		else:
			while abs(y) < abs(y2):
				y += 1
				points.append([round(x1), round(y)])
		
		self.draw(points)
		t2 = time.clock()
		print("Assymetric DDA:")
		print(t2 - t1)
	
	def Bresenham(self, x1, y1, x2, y2):
		t1 = time.clock()
		# Setup initial conditions
		dx = x2 - x1
		dy = y2 - y1
		# Determine how steep the line is
		is_steep = abs(dy) > abs(dx)
		# Rotate line
		if is_steep:
			x1, y1 = y1, x1
			x2, y2 = y2, x2
		# Swap start and end points if necessary
		if x1 > x2:
			x1, x2 = x2, x1
			y1, y2 = y2, y1
		
		# Recalculate differentials
		dx = x2 - x1
		dy = y2 - y1
		
		# Calculate error
		error = int(dx / 2.0)
		ystep = 1 if y1 < y2 else -1
		
		# Iterate over bounding box generating points between start and end
		y = y1
		points = []
		for x in range(x1, x2 + 1):
			coord = (y, x) if is_steep else (x, y)
			points.append(coord)
			error -= abs(dy)
			if error < 0:
				y += ystep
				error += dx
		self.draw(points)
		t2 = time.clock()
		print("Bresenham:")
		print(t2 - t1)
	
	def circle_Bresenham(self, xc, yc, radius):
		t1 = time.clock()
		x = 0
		y = radius
		delta = 1 - 2 * radius
		error = 0
		points = []
		while (y >= 0):
			points.append((xc + x, yc + y))
			points.append((xc + x, yc - y))
			points.append((xc - x, yc + y))
			points.append((xc - x, yc - y))
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
		self.draw(points)
		t2 = time.clock()
		print("Circle Bresenham:")
		print(t2 - t1)
	
	def elipse_Bresenham(self, xc, yc, radius, b):
		t1 = time.clock()
		x = 0
		y = radius
		delta = 1 - 2 * radius
		error = 0
		points = []
		if radius > b:
			while (y >= 0):
				points.append((xc + x, yc + y))
				points.append((xc + x, yc - y))
				points.append((xc - x, yc + y))
				points.append((xc - x, yc - y))
				error = 2 * (delta + y) - 1
				if (delta < 0) and (error <= 0):
					x += 1
					delta += 2 * x + 1
					continue
				error = 2 * (delta - x) - 1
				if delta > 0 and error > 0:
					y -= b / radius
					delta += 1 - 2 * y
					continue
				x += 1
				delta += 2 * (x - y)
				y -= b / radius
		self.draw(points)
		t2 = time.clock()
		print("Elipse Bresenham:")
		print(t2 - t1)
	
	def Wu(self, x1, y1, x2, y2):
		t1 = time.clock()
		
		def _fpart(x):
			return x - int(x)
		
		def _rfpart(x):
			return 1 - _fpart(x)
		
		points = []
		dx, dy = x2 - x1, y2 - y1
		x, y = x1, y1
		
		if dy == 0:
			points.append([round(x), round(y1)])
			while abs(x) < abs(x2):
				x += 1
				points.append([round(x), round(y1)])
		
		elif dx == 0:
			points.append([round(x1), round(y)])
			while abs(y) < abs(y2):
				y += 1
				points.append([round(x1), round(y)])
		else:
			grad = dy / dx
			intery = y1 + _rfpart(x1) * grad
			
			def draw_endpoint(x, y):
				xend = round(x)
				yend = y + grad * (xend - x)
				px, py = int(xend), int(yend)
				points.append([px, py])
				points.append([px, py + 1])
				return px
			
			xstart = draw_endpoint(x1, y1)
			xend = draw_endpoint(x2, y2)
			
			for x in range(xstart, xend):
				y = int(intery)
				points.append([x, y])
				points.append([x, y + 1])
				intery += grad
		self.draw(points)
		t2 = time.clock()
		print("Wu:")
		print(t2 - t1)
	
	def draw(self, coords):
		for point in coords:
			self.canvas.create_rectangle(PIXEL_SIZE * point[0], PIXEL_SIZE * point[1],
										 PIXEL_SIZE * point[0] + PIXEL_SIZE, PIXEL_SIZE * point[1] + PIXEL_SIZE,
										 fill="black", tag="surname")
	
	def clean(self):
		self.canvas.delete("surname")
	
	def callback(self, func_name):
		if func_name == "elipse_Bresenham":
			return lambda func_name=func_name: getattr(self, func_name)(85, 60, 15, 5)
		if func_name != "circle_Bresenham":
			def func():
				for letter, lines in self.surname.items():
					for line in lines:
						if letter == "o":
							getattr(self, "circle_Bresenham")(line[0][0], line[0][1], line[1][0])
						else:
							t1 = time.clock()
							getattr(self, func_name)(line[0][0], line[0][1], line[1][0], line[1][1])
			
			return func
		return lambda func_name=func_name: getattr(self, func_name)(85, 60, 15)
	
	def __init__(self):
		window = tk.Tk()
		window.title("Lab1 Brykalova")
		# Place canvas in the window
		self.canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg="light blue")
		self.canvas.pack()
		# Draw Frame in the window
		frame = tk.Frame(window, bg="light blue")
		frame.pack()
		dda_btn = tk.Button(frame, text="       DDA      ", command=self.callback("DDA"))
		dda_btn.grid(row=1, column=1)
		as_dda_btn = tk.Button(frame, text=" Assymetric DDA ", command=self.callback("assymetric_DDA"))
		as_dda_btn.grid(row=1, column=2)
		bres_btn = tk.Button(frame, text="    Bresenham   ", command=self.callback("Bresenham"))
		bres_btn.grid(row=1, column=3)
		circle_bres_btn = tk.Button(frame, text="Circle Bresenham", command=self.callback("circle_Bresenham"))
		circle_bres_btn.grid(row=1, column=4)
		elipse_bres_btn = tk.Button(frame, text="Elipse Bresenham", command=self.callback("elipse_Bresenham"))
		elipse_bres_btn.grid(row=1, column=5)
		wu_btn = tk.Button(frame, text="       Wu       ", command=self.callback("Wu"))
		wu_btn.grid(row=1, column=6)
		clear_btn = tk.Button(frame, text="      Clear     ", command=self.clean)
		clear_btn.grid(row=1, column=7)
		window.mainloop()


if __name__ == "__main__":
	RasterizationAlgorithms()
