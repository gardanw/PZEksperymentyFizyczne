import numpy as np
import matplotlib.pyplot as plt
import tkinter

class Body:
    g = 1.5 #6.6743 * 10 ** (-11)
    mcpos = [] #lista polozen srodka masy
    def __init__(self, mass, pos, v, a):
        self.mass = mass
        self.pos = [pos] #lista 2elementowych tablic numpy, czyli caly przebyty tor
        self.v = [v] #lista 2elementowych tablic numpy, czyli cala historia predkosci
        self.a = a #2elementowa tablica numpy

    def difference_len(v1, v2): #dlugosc wektora laczacego konce 2 wektorow podniesiona do 3 potegi w 2D
        return ((v1[0]-v2[0])**2 + (v1[1]-v2[1])**2)**(3/2)

    def mass_center(obj1, obj2, obj3): #wspolrzedne srodka masy w ostatniej sytuacji
        mcpos = []
        for i in range(2):
            mcpos.append((obj1.mass*obj1.pos[-1][i] + obj2.mass*obj2.pos[-1][i] + obj3.mass*obj3.pos[-1][i])/(obj1.mass + obj2.mass + obj3.mass))
        return mcpos

    def leapfrog(self, dt, obj1, obj2): #dodaje nowe polozenie do listy, nowa predkosc do listy, liczy a
        pos_temp = self.pos[-1].copy()
        v_temp = self.v[-1].copy()
        self.v.append(v_temp + 0.5*self.a*dt)
        self.pos.append(pos_temp + self.v[-1]*dt)
        self.a = self.g *(obj1.mass*(obj1.pos[-1]-self.pos[-1])/Body.difference_len(self.pos[-1], obj1.pos[-1]) + obj2.mass*(obj2.pos[-1]-self.pos[-1])/Body.difference_len(self.pos[-1], obj2.pos[-1]))
        self.v[-1] += 0.5*self.a*dt


class Simulation:
    def run(N, dt): #generowanie torow ruchu dla podanych liczby powtorzen i kroku czasowego
        for i in range(N):
            body1.leapfrog(dt, body2, body3)
            body2.leapfrog(dt, body1, body3)
            body3.leapfrog(dt, body1, body2)
            Body.mcpos.append(Body.mass_center(body1, body2, body3)) #aktualizuje polozenie srodka masy, chyba powinien caly czas stac w miejscu...
        #print(body1.pos, body2.pos, body3.pos) #mozna odkomentowac w zaleznosci od potrzeb
        '''
        mozna jeszcze zrobic taka wersje wizualizacji, ze do latajacych cial beda
        przyczepione wektory predkosci, ktore beda sie odpowiednio krecic, zwiekszac zmiejszac,
        zeby pokazywac predkosc chwilowa ciala --> Body.v jest lista kolejnych predkosci,
        wiec nie powinno to byc trudne
        '''

    def draw(obj1, obj2, obj3, obj4): #rysowanie symulacji
        size = 10 #zmniejszajac size "przybliza sie" symulacje
        l_krokow = 1000
        l_ruchow = 3
        root = tkinter.Tk()
        window_size = 500
        canvas = tkinter.Canvas(root, width=window_size, height=window_size, bg="#fff")
        canvas.pack()
        for i in range(len(obj1)):
            pos = [obj1[i], obj2[i], obj3[i], obj4[i]]
            s = window_size/size
            dx = 0.01
            colors = ["red", "blue", "green", "gray"]
            for k in range(4):
                coords = (pos[k][0]-dx)*s+window_size/2, (pos[k][1]-dx)*s+window_size/2, (pos[k][0]+dx)*s+window_size/2, (pos[k][1]+dx)*s+window_size/2
                canvas.create_rectangle(coords, outline=colors[k])
                canvas.update()
            
if __name__=='__main__':
    #warunki poczatkowe
    '''
    #wersja z losowaniem:
    body1 = Body(10.0, np.random.rand(2)*4-2, np.array([0., 0.]), np.array([0., 0.]))
    body2 = Body(10.0, np.random.rand(2)*4-2, np.array([0., 0.]), np.array([0., 0.]))
    body3 = Body(10.0, np.random.rand(2)*4-2, np.array([0., 0.]), np.array([0., 0.]))
    
    #wersja z dobieraniem warunkow poczatkowych:
    body1 = Body(10.0, np.array([0.7, 0.6]), np.array([0., 0.]), np.array([0., 0.]))
    body2 = Body(10.0, np.array([-0.9, 0.2]), np.array([0., 0.]), np.array([0., 0.]))
    body3 = Body(10.0, np.array([1., -1.]), np.array([0., 0.]), np.array([0., 0.]))
    '''
    #uklad w stylu slonce-ziemia-ksiezyc
    body1 = Body(1000.0, np.array([0.0, 0.0]), np.array([0., 0.]), np.array([0., 0.]))
    body2 = Body(2.0, np.array([4.0, 0.0]), np.array([0., 7.]), np.array([0., 0.]))
    body3 = Body(0.01, np.array([4., 0.04]), np.array([7., 0.]), np.array([0., 0.]))
    
    N = 5000
    #N = np.random.randint(10, 10000) #do wyboru wersja z losowym N
    dt = 0.001 
    #dt = np.random.random()*0.003 + 0.0001 #do wyboru wersja z losowym krokiem czasowym

    print('Liczba krokow:', N, 'krok czasowy:', dt)
    Simulation.run(N, dt)
    print('Przemieszczenie srodka masy: od', Body.mcpos[0], 'do', Body.mcpos[N-1])

    print('1. cialo: polozenie poczatkowe:', body1.pos[0]) #, 'predkosc poczatkowa:', body1.v[0])
    print('2. cialo: polozenie poczatkowe:', body2.pos[0]) #, 'predkosc poczatkowa:', body2.v[0])
    print('3. cialo: polozenie poczatkowe:', body3.pos[0]) #, 'predkosc poczatkowa:', body3.v[0])
    
    Simulation.draw(body1.pos, body2.pos, body3.pos, Body.mcpos)

    '''
    efekt koncowy mocno zalezy od warunkow poczatkowych,
    a tu jest wyzwanie z sensownym ich dobraniem.
    '''
