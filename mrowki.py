import tkinter
coord_moves = {
    "R": {(0, -1): (-1, 0), (-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1)},
    "L": {(0, -1): (1, 0), (1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1)},
} #kierunek ruchu mrówki
def plansza(size):
    return [[0 for _ in range(size)] for _ in range(size)]

size = 111 #rozmiar planszy po której będzie chodzić mrówka
board = plansza(size) #tworzę planszę po której będzie chodzić mrówka
x, y = size // 2, size // 2 #pole na którym znajduje się mrówka
liczba_krokow=10000 #liczba kroków wykonanaych prez mrówkę w symulacji
liczba_ruchow=1 #liczba kroków wykonanych przez mrówkę przy jednej aktualizacji canwy
koordynanty = (0, -1) #koordynanty
pattern = "RL" #możliwe kierunki obrotu i ruchu mrówki
root = tkinter.Tk()
window_size = 400 #rozmiar okna
canvas = tkinter.Canvas(root, width=window_size, height=window_size, bg="#fff")
canvas.pack()
def redraw(window_size, size, canvas, board): #dzięki temu pokazujemy stopniowe rysowanie ruchu mrówki
    s = window_size / size
    canvas.delete("all")
    for y, row in enumerate(board):
        for x, field in enumerate(row):
            color = "white" if field == 0 else "black"
            if field:
                canvas.create_rectangle(
                    s * x, s * y, s + (s * x), s + (s * y), fill=color, outline=color
                )
    canvas.update() #dzięki temu pokazujemy stopniowe rysowanie ruchu mrówki

try: #sytuacja w której mrówka może się zderzyć ze ścianą- zatrzymanie programu i print maksymalnej liczby kroków
    for i in range(liczba_krokow): #liczba+1 to liczba wykonanych kroków
        field = board[y][x] #współrzędne pola mrówki
        direction = pattern[field] #kierunek ruchu mrówki
        board[y][x] = (field + 1) % len(pattern) #kierunek ruchu mrówki
        koordynanty = coord_moves[direction][koordynanty]
        y, x = y + koordynanty[0], x + koordynanty[1]

        if y < 0 or x < 0: #bez tego fragmentu jeśli nie dajemy warunku ze ściną
            raise IndexError

        if not (i % liczba_ruchow): #liczba+1 to liczba co ile ruchów mrówki ma być aktualizowana canva
            redraw(window_size, size, canvas, board)
except IndexError:
    print(i) #maksymalna liczba kroków dla danego rozmiaru planszy

redraw(window_size, size, canvas, board)
root.mainloop()
