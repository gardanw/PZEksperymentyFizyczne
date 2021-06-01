import tkinter

import numpy as np
from scipy.constants import constants


def rgb_to_hex(rgb):
    r, g, b = rgb
    return f'#{r:02x}{g:02x}{b:02x}'


def random_body(n, dim):
    l_b = []
    for _ in range(n):
        l_b.append(Body(100 * np.random.random() + 1, 10 * np.random.random_sample((dim,)) - 5,
                        np.random.random_sample((dim,)), np.zeros(dim)))
    return l_b


def calc_distance(b1, b2):
    return np.sqrt(sum([(b1.pos[-1][i] - b2.pos[-1][i]) ** 2 for i in range(len(b1.pos[-1]))]))


def calc_versor(b1, b2):
    return (b1.pos[-1] - b2.pos[-1]) / calc_distance(b1, b2)


def calc_mas_center(l_body):
    sum_m = sum([b.m for b in l_body])
    sum_mpos = sum([b.m * b.pos[-1] for b in l_body])
    return sum_mpos / sum_m


def correction_v(l_body):
    sum_m = sum([b.m for b in l_body])
    sum_mv = sum([b.m * b.v[-1] for b in l_body])
    for b in l_body:
        b.v[-1] -= sum_mv / sum_m


class Body:
    def __init__(self, m, pos, v, f):
        self.m = m
        self.pos = [pos]
        self.v = [v]
        self.f = f


class Simulation:
    def __init__(self, l_body, dimension):
        self.l_body = l_body
        self.dt = 0.001
        # self.G = constants.G * 10 ** 8
        self.G = 1
        self.dimension = dimension
        self.mc = [calc_mas_center(l_body)]
        correction_v(l_body)

    def leap_frog(self):
        for b in self.l_body:
            b.v.append(b.v[-1] + b.f * self.dt / b.m)
            b.pos.append(b.pos[-1] + b.v[-1] * self.dt)

    def calc_f(self):
        for b1 in self.l_body:
            f = np.zeros(self.dimension)
            for b2 in self.l_body:
                if b2 != b1:
                    f += (self.G * b1.m * b2.m / calc_distance(b1, b2) ** 2) * calc_versor(b2, b1)
            b1.f = f

    def run(self, n=1, dodraw=False, take_data=False):
        for i in range(n):
            self.calc_f()
            self.leap_frog()
            self.mc.append(calc_mas_center(self.l_body))
        if dodraw:
            self.draw()
        if take_data:
            return [[b.pos for b in self.l_body], [b.v[-1] for b in self.l_body]]

    def draw(self):
        size = 10
        root = tkinter.Tk()
        window_size = 800
        canvas = tkinter.Canvas(root, width=window_size, height=window_size, bg="#fff")
        canvas.pack()
        colors = [rgb_to_hex((np.random.randint(255), np.random.randint(255), np.random.randint(255))) for _ in
                  range(len(self.l_body) + 1)]
        is_error = 0
        while True:
            pos = [b.pos[-1] for b in self.l_body]
            pos.append(self.mc[-1])
            s = window_size / size
            dx = 0.02
            for k in range(len(pos)):
                coords = (pos[k][0] - dx) * s + window_size / 2, (pos[k][1] - dx) * s + window_size / 2, (
                        pos[k][0] + dx) * s + window_size / 2, (pos[k][1] + dx) * s + window_size / 2
                try:
                    canvas.create_rectangle(coords, outline=colors[k])
                    canvas.update()
                except tkinter.TclError:
                    is_error = -1
                    break
            if is_error == -1:
                break
            self.run()


if __name__ == '__main__':
    dim = 2
    # n = np.random.randint(10)+2
    n = 3
    print(n)

    b1 = Body(1, np.array([0.2, 0.6]), np.array([0., 0.]), np.array([0., 0.]))
    b2 = Body(1, np.array([-0.9, 0.2]), np.array([0., 0.]), np.array([0., 0.]))
    b3 = Body(1, np.array([1., -1.]), np.array([0., 0.]), np.array([0., 0.]))

    l_b = [b1, b2, b3]

    body1 = Body(133200.0, np.array([0.0, 0.0]), np.array([0., 0.]), np.array([0., 0.]))
    body2 = Body(4, np.array([4.0, 0.0]), np.array([0., -15.]), np.array([0., 0.]))
    body3 = Body(0.0492, np.array([4.0, 0.0416]), np.array([-0.9, -15.0]), np.array([0., 0.]))

    # l_b = [body1, body2, body3]

    # l_b = random_body(n, dim)

    s = Simulation(l_b, dim)
    # s.run(5000)
    s.draw()