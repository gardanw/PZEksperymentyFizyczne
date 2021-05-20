import numpy as np
import matplotlib.pyplot as plt
import tkinter

class Body:
    g = 6.6743 * 10**(-11)
    mcpos = [] #lista polozen srodka masy
    def __init__(self, mass, pos, v, a):
        self.mass = mass
        self.pos = [pos] #lista 3elementowych tablic numpy, czyli caly przebyty tor
        self.v = [v] #lista 3elementowych tablic numpy, czyli cala historia predkosci
        self.a = a #3elementowa tablica numpy

    def difference_len(v1, v2): #dlugosc wektora laczacego konce 2 wektorow podniesiona do 3 potegi
        return ((v1[0]-v2[0])**2 + (v1[1]-v2[1])**2 + (v1[2]-v2[2])**2)**(3/2)

    def mass_center(obj1, obj2, obj3): #wspolrzedne srodka masy w ostatniej sytuacji
        mcpos = []
        for i in range(3):
            mcpos.append((obj1.mass*obj1.pos[-1][i] + obj2.mass*obj2.pos[-1][i] + obj3.mass*obj3.pos[-1][i])/(obj1.mass + obj2.mass + obj3.mass))
        return mcpos

    def leapfrog(self, dt, obj1, obj2): #dodaje nowe polozenie do listy, nowa predkosc do listy, liczy a
        pos_temp = self.pos[-1].copy()
        v_temp = self.v[-1].copy()
        self.v.append(v_temp + 0.5*self.a*dt)
        self.pos.append(pos_temp + self.v[-1]*dt)
        #przyspieszenie nie pomnozone przez g:
        self.a = (obj1.mass*(obj1.pos[-1]-self.pos[-1])/Body.difference_len(self.pos[-1], obj1.pos[-1]) + obj2.mass*(obj2.pos[-1]-self.pos[-1])/Body.difference_len(self.pos[-1], obj2.pos[-1]))
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

    def draw(obj1, obj2, obj3, obj4): #wizualizacja w dwoch wymiarach (czyli trzeci nie jest wgl wziety pod uwage!); funkcja robocza
        size = 10 #zmniejszajac size "przybliza sie" symulacje
        root = tkinter.Tk()
        window_size = 400
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
    body1 = Body(10.0, np.random.rand(3)*4-2, np.random.rand(3)-0.5, np.array([0., 0., 0.]))
    body2 = Body(10.0, np.random.rand(3)*4-2, np.random.rand(3)-0.5, np.array([0., 0., 0.]))
    body3 = Body(10.0, np.random.rand(3)*4-2, np.random.rand(3)-0.5, np.array([0., 0., 0.]))
    
    #wersja z tak dobieraniem warunkow poczatkowych:
    body1 = Body(10.0, np.array([2., 1., 1.]), np.array([0., 0., 0.]), np.array([0., 0., 0.]))
    body2 = Body(10.0, np.array([-0.4, 0.5, 1.4]), np.array([0., 0., 0.]), np.array([0., 0., 0.]))
    body3 = Body(10.0, np.array([-1., -0.4, -0.2]), np.array([0., 0., 0.]), np.array([0., 0., 0.]))
    
    #przykladowe warunki poczatkowe
    body1 = Body(10.0, np.array([-1.1023784,   0.43453602, -1.30941989]), np.array([-0.49706766,  0.37358589, -0.47687343]), np.array([0., 0., 0.]))
    body2 = Body(10.0, np.array([ 0.4976821,   0.42468692, -1.20891154]), np.array([-0.4002198,  -0.40555012, -0.4453577]), np.array([0., 0., 0.]))
    body3 = Body(10.0, np.array([0.87299781, -1.08513693,  0.33903255]), np.array([0.19242201, 0.37130446, 0.47556433]), np.array([0., 0., 0.]))
    '''
    #przykladowe warunki poczatkowe
    body1 = Body(10.0, np.array([ 1.0843712,  -0.61777304, -0.90709771]), np.array([ 0.47839862,  0.13894337, -0.43962597]), np.array([0., 0., 0.]))
    body2 = Body(10.0, np.array([-1.49024846,  1.45539006,  0.71866011]), np.array([ 0.43633095, -0.35867242,  0.3587824 ]), np.array([0., 0., 0.]))
    body3 = Body(10.0, np.array([-0.26843371,  0.58914631, -1.9438411 ]), np.array([0.03909739, 0.3148738,  0.13320261]), np.array([0., 0., 0.]))
    
    
    N = 10000
    #N = np.random.randint(10, 10000) #do wyboru wersja z losowym N
    dt = 0.001 
    #dt = np.random.random()*0.003 + 0.0001 #do wyboru wersja z losowym krokiem czasowym

    print('Liczba krokow:', N, 'krok czasowy:', dt)
    Body.mcpos.append(Body.mass_center(body1, body2, body3))
    Simulation.run(N, dt)
    #print('Przemieszczenie srodka masy: od', Body.mcpos[0], 'do', Body.mcpos[-1])

    print('1. cialo: polozenie poczatkowe:', body1.pos[0], 'predkosc poczatkowa:', body1.v[0])
    print('2. cialo: polozenie poczatkowe:', body2.pos[0], 'predkosc poczatkowa:', body2.v[0])
    print('3. cialo: polozenie poczatkowe:', body3.pos[0], 'predkosc poczatkowa:', body3.v[0])
   
    Simulation.draw(body1.pos, body2.pos, body3.pos, Body.mcpos)
    
    
    '''
    efekt koncowy mocno zalezy od warunkow poczatkowych,
    a tu jest wyzwanie z sensownym ich dobraniem.
    '''
