from browser import html, document, console, alert,timer
from visualife.core import HtmlViewport
from visualife.calc.math_utils import regular_polygon
from visualife.core.CanvasViewport import CanvasViewport
coord_moves = {
    "R": {(0, -1): (-1, 0), (-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1)},
    "L": {(0, -1): (1, 0), (1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1)},
} #kierunek ruchu mrówki

cnvs = document["canvas"].getContext("2d")
drawing = CanvasViewport(cnvs, 700,700)

def plansza(size):
    p = [[0 for _ in range(size)] for _ in range(size)]
    draw(p)
    return p

def draw(board):
    b = ''
    for i in board:
        b += ''.join(map(str, i))
    drawing.binary_map_2(b, size, size)


size = 15 #rozmiar planszy po której będzie chodzić mrówka
board = plansza(size) #tworzę planszę po której będzie chodzić mrówka
x, y = size // 2, size // 2 #pole na którym znajduje się mrówka
koordynanty = (0, -1) #koordynanty
pattern = "RL" #możliwe kierunki obrotu i ruchu mrówki
idtimer = 1

def simulate():
    global x, y, koordynanty, board, idtimer
    try: #sytuacja w której mrówka może się zderzyć ze ścianą- zatrzymanie programu i print maksymalnej liczby kroków
        field = board[y][x] #współrzędne pola mrówki
        direction = pattern[field] #kierunek ruchu mrówki
        board[y][x] = (field + 1) % len(pattern) #kierunek ruchu mrówki
        koordynanty = coord_moves[direction][koordynanty]
        y, x = y + koordynanty[0], x + koordynanty[1]

        if y < 0 or x < 0: #bez tego fragmentu jeśli nie dajemy warunku ze ściną
            raise IndexError

        draw(board) #update wizualizacji

    except IndexError:
        timer.clear_interval(idtimer)
        idtimer = 1

def start_sim(evt):
    global idtimer
    idtimer = timer.set_interval(simulate,100)

def stop_sim(evt):
    global idtimer
    timer.clear_interval(idtimer)
    idtimer = 1
    print("stop")

def restart_sim(evt):
    global x, y, koordynanty, board, idtimer
    stop_sim(evt)
    board = plansza(size)
    x, y = size // 2, size // 2
    koordynanty = (0, -1)

document["start"].bind("click",start_sim)
document["stop"].bind("click",stop_sim)
document["restart_sim"].bind("click",restart_sim)