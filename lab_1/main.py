import numpy as np
import time


class Dot:
    x = None
    y = None

    def __init__(self, x: float, y:float):
        self.x = x
        self.y = y

    def __eq__(self, obj: object) -> bool:
        if self.x == obj.x and self.y == obj.y:
            return True
        return False

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)


def DDA(dot_1: Dot, dot_2: Dot) -> None:
    start_time = time.clock()
    if np.abs(dot_2.x - dot_1.x) >= np.abs(dot_2.y - dot_1.y):
        length = np.abs(dot_2.x - dot_1.x)
    else:
        length = np.abs(dot_2.y - dot_1.y)

    delta_x = (dot_2.x - dot_1.x) / length
    delta_y = (dot_2.y - dot_1.y) / length

    print('Output --> {}'. format(time.clock() - start_time))


if __name__ == '__main__':

    dot1 = Dot(x=0, y=0)
    dot2 = Dot(x=1, y=2)
    print('dot1 = {}, dot2 = {}'.format(dot1, dot2))

    DDA(dot1, dot2)
