import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import math
import numpy as np


class myRectangle:
    def __init__(self, pts) -> None:
        self.pts = pts

class myTriangle:
    def __init__(self, pts, w, h) -> None:
        self.pts = pts


class myHexagon:
    def __init__(self, pts) -> None:
        self.pts = pts
#subplots
#что из себя представляет fig, ax = plt.subplots()
def draw(all_figures, lim_y=20, lim_y_m=-20, lim_x=20, lim_x_m=-20):
    fig, ax = plt.subplots()
    ax.plot([0, lim_x], [0, 0])
    ax.plot([0, 0], [0, lim_y])
    ax.plot([0, lim_x_m], [0, 0])
    ax.plot([0, 0], [0, lim_y_m])
    for figures in all_figures:
        for figure in figures:
            if isinstance(figure, myRectangle):
                p = Polygon(figure.pts, closed=False)
                ax.add_patch(p)
            if isinstance(figure, myTriangle):
                p = Polygon(figure.pts, closed=False)
                ax.add_patch(p)
                #Что он тут делает? isinstance(figure, myHexagon)
            if isinstance(figure, myHexagon):
                p = Polygon(figure.pts, closed=False)
                #add_patch как нам помогает с fig, ax = plt.subplots()
                ax.add_patch(p)
    plt.show()

# w = ширина , h = высота, с = кол-во раз
def gen_rectangle(x, y, h, w, c, w_x=0, w_y=0):
    arr = []
    for i in range(0, c):
        pts = [[x, y], [x + w, y], [x + w, y + h], [x, y + h]]
        arr.append(myRectangle(pts))
        x += w + w_x
        if w_y != 0:
            y += h + w_y
    return arr


def gen_triangle(x, y, h, w, c, w_x=0, w_y=0):
    arr = []
    for i in range(0, c):
        pts = [[x, y], [x + w, y], [x + w/2, y + h]]
        arr.append(myTriangle(pts, w, h))
        x += w + w_x
        if w_y != 0:
            y += h + w_y
    return arr


def gen_hexagon(x, y, h, w, c, w_x=0, w_y=0):
    arr = []
    for i in range(0, c):
        pts = [[x, y], [x + w, y], [x + w + w/2, y + h/2],
               [x + w, y + h], [x, y + h], [x-w/2, y+h/2]]
        arr.append(myHexagon(pts))
        x += w + w_x
        if w_y != 0:
            y += h + w_y
    return arr


def gen_mixed(x, y, h, w, c, w_x=0, w_y=0):
    arr = []
    curr_x, curr_y = x, y
    for i in range(1, c + 1):
        figure = 0
        if i % 2 == 0:
            print('rect')
            figure = gen_rectangle(curr_x, curr_y, h, w, 1, w_x, w_y)
        elif i % 3 == 0:
            print('hex')
            figure = gen_hexagon(curr_x, curr_y, h, w, 1, w_x, w_y)
        else:
            print('triang')
            figure = gen_triangle(curr_x, curr_y, h, w, 1, w_x, w_y)
        arr.append(*figure)
        if w_x != 0:
            curr_x += w + w_x
        if w_y != 0:
            curr_y += h + w_y
    return arr


def tr_translate(figures, x_w, y_w):
    for figure in figures:
        if isinstance(figure, myRectangle):
            for point in figure.pts:
                # где здесь шаг? Чем он заменен*
                point[0] += x_w
                point[1] += y_w
        if isinstance(figure, myTriangle):
            for point in figure.pts:
                point[0] += x_w
                point[1] += y_w
        if isinstance(figure, myHexagon):
            for point in figure.pts:
                point[0] += x_w
                point[1] += y_w


def rotate_point(x, y, a, m, n):
    #a = альфа + гамма
    # Как со списком характеристик а происходит это
    a = math.radians(a)
    matrix1 = np.array([[x, y, 1]])
    t_a = -1*m*(math.cos(a)-1)+n*math.sin(a)
    print(math.cos(a),math.sin(a))
    #m=x,n=y
    #x=x0,y=y0
    t_b = -1*n*(math.cos(a)-1)-m*math.sin(a)
    print(math.cos(a), math.sin(a))
    #m=y,n=x
    # x=x0,y=y0
    #matrix2=[x,y,l]
    #np.array - что делает с двойным массивом?
    matrix2 = np.array([[math.cos(a), math.sin(a), 0],
                        [-1*math.sin(a), math.cos(a), 0],
                        [t_a, t_b, 1]])
    total = matrix1.dot(matrix2)
    x, y, l = total[0]
    return x, y


def tr_rotate(x0, y0, figures, a):
    for figure in figures:
        if isinstance(figure, myTriangle):
            for point in figure.pts:
                point[0], point[1] = \
                    rotate_point(point[0], point[1], a, x0, y0)
                #point[0]*cos(a)
                #point[0]*sin(a)
                print(point[0],point[1])
        if isinstance(figure, myRectangle):
            for point in figure.pts:
                print(point[0],point[1])
                point[0], point[1] = \
                    rotate_point(point[0], point[1], a, x0, y0)
                print(point[0], point[1])
        if isinstance(figure, myHexagon):
            for point in figure.pts:
                point[0], point[1] = \
                    rotate_point(point[0], point[1], a, x0, y0)
                print(point[0], point[1])


def sym_triangle(figure):
    #Когда сумма не меняется? Поговорка.
    y0 = figure.pts[2][1]
    y1 = figure.pts[0][1]
    figure.pts[0][1] = y0
    figure.pts[1][1] = y0
    figure.pts[2][1] = y1


def tr_symmetry(figures, x_w=0, y_w=0):
    #аналог транслейт
    for figure in figures:
        if isinstance(figure, myTriangle):
            sym_triangle(figure)
            for point in figure.pts:
                point[0] += x_w
                point[1] += y_w


def homothety_point(x, y, k, m, n):
    #k = характеристики массива, m n - ?
    x = k*x + m*(1-k)
    y = k*y + n*(1-k)
    return x, y


def tr_homothety(x0, y0, figures, k, k_step):
    for figure in figures:
        if isinstance(figure, myTriangle):
            for point in figure.pts:
                point[0], point[1] = \
                    homothety_point(point[0], point[1], k, x0, y0)
        if isinstance(figure, myRectangle):
            for point in figure.pts:
                point[0], point[1] = \
                    homothety_point(point[0], point[1], k, x0, y0)
        if isinstance(figure, myHexagon):
            for point in figure.pts:
                point[0], point[1] = \
                    homothety_point(point[0], point[1], k, x0, y0)
        k += k_step


# №4.1
rects0 = gen_rectangle(-20, 0, 2, 4, 9, 1, 0)
rects1 = gen_rectangle(-20, 5, 2, 4, 9, 1, 0)
rects2 = gen_rectangle(-20, -5, 2, 4, 9, 1, 0)
tr_rotate(0, 0, rects0, 40)
tr_rotate(0, 0, rects1, 40)
tr_rotate(0, 0, rects2, 40)
draw([rects0, rects1, rects2], 25, -25, 25, -25)

# №4.2
rects0 = gen_rectangle(-20, 0, 2, 4, 9, 1, 0)
rects1 = gen_rectangle(-20, 10, 2, 4, 9, 1, 0)
tr_rotate(0, 0, rects0, 30)
tr_rotate(10, 5, rects1, -25)
tr_translate(rects1, 0, -8)
draw([rects0, rects1], 25, -25, 25, -25)

# №4.3
triang0 = gen_triangle(-18, 0, 3, 3, 12, 0, 0)
triang1 = gen_triangle(-18, 0, 3, 3, 12, 0, 0)
tr_symmetry(triang1, 0, 4)
draw([triang0, triang1])

# №4.4
rects0 = gen_rectangle(0, 0, 4, 2, 5, 1, 0)
tr_rotate(0, 0, rects0, 45)
tr_homothety(0, 0, rects0, 1.5, 0.5)
tr_translate(rects0, 4, 0)
rects1 = gen_rectangle(0, 0, 4, 2, 5, 1, 0)
tr_rotate(0, 0, rects1, 225)
tr_homothety(0, 0, rects1, 1.5, 0.5)
tr_translate(rects1, -4, 0)
draw([rects0, rects1], 40, -40, 40, -40)


# figs1 = gen_mixed(0, 0, 4, 2, 5, 2, 0)
# draw([figs1])
