import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

def rot_point(point, rot_centre): #obraca punkt o 90 stopni w kierunku ujemnym wzgledem zadanego srodka
    temp = point.copy() - rot_centre
    return np.array([temp[1]+rot_centre[0], -temp[0]+rot_centre[1]])
    
def draw(points, N): #aktualizuje obrazek
    for i in range(N//2, N):
        coords = (points[i-1, 0]*s+window_size*3/8, points[i-1, 1]*s+window_size*2/3, points[i, 0]*s+window_size*3/8, points[i, 1]*s+window_size*2/3)
        canvas.create_line(coords, fill="green")
    canvas.update()
    
def rotation(points): #do listy punktow dodaje ich odbicia po obrocie
    N = len(points)
    rot_centre = points[-1]
    for i in range(N-2, -1, -1):
        points = np.append(points, [rot_point(points[i], rot_centre)], axis=0)
    draw(points, N)
    return(points)
        

#warunki poczatkowe dla obrazka
size = 350 #zmniejszajac size, mozna "przyblizyc" obrazek
root = tk.Tk()
window_size = 500
s = window_size/size
canvas = tk.Canvas(root, width=window_size, height=window_size, bg="#af4") #losowy smoczy kolor:)
canvas.pack()

points = np.array([[0., 0.], [1., 0.]]) #zaczyna sie od pojedynczego odcinka
N = 16 #liczba obrotow istniejacego obrazka o 90 stopni
for i in range(N):
    points = rotation(points)




