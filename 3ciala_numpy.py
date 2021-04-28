import numpy as np
import matplotlib.pyplot as plt
#from ipywidgets import interact

class Body:
    g = 6.6743 * 10**(-11)
    mcpos = [] #lista polozen srodka masy
    def __init__(self, mass, pos, v, a):
        self.mass = mass
        self.pos = [pos] #lista 3elementowych tablic numpy, czyli caly przebyty tor
        self.v = [v] #lista 3elementowych tablic numpy, czyli cala historia predkosci
        self.a = a #3elementowa tablica numpy

    def difference_len(v1, v2): #dlugosc wektora laczacego konce 2 wektorow podniesiona do 3 potegi w 2D
        return ((v1[0]-v2[0])**2 + (v1[1]-v2[1])**2 + (v1[2]-v2[2])**2)**(3/2)

    def vec_len(v): #do generowania wykresu predkosci: liczy wartosci kolejnych predkosci w 2D
        vec_len_list = []
        for i in range(len(v)):
            vec_len_list.append(np.sqrt((v[i][0])**2 + (v[i][1])**2 + (v[i][2])**2))
        return vec_len_list

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
        self.a = self.g*(obj1.mass*(obj1.pos[-1]-self.pos[-1])/Body.difference_len(self.pos[-1], obj1.pos[-1]) + obj2.mass*(obj2.pos[-1]-self.pos[-1])/Body.difference_len(self.pos[-1], obj2.pos[-1]))
        self.v[-1] += 0.5*self.a*dt

    def track(self):
        #w tej wersji rysuje wykres odleglosci od pkt (0, 0) w zaleznosci od czasu; bardziej miarodajny bylaby odleglosc od srodka masy
        ox = np.linspace(0, N*dt, N+1)
        oy = []
        for i in range(N+1):
            oy.append((self.pos[i][0]**2 + self.pos[i][1]**2 + self.pos[i][2]**2)**(1/2))
        plt.plot(ox, oy)
        #plt.show()
        
        #w tej wersji zaznacza punkty o wspolrzednych kolejnych polozen (dwuwymiarowe)
        #plt.plot([x[0] for x in self.pos], [x[1] for x in self.pos])
        #plt.show()

class Simulation:
    def run(N, dt): #generowanie torow ruchu dla podanych liczby powtorzen i kroku czasowego
        print('Liczba krokow:', N, 'krok czasowy:', dt)
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

    def v_plot(N, dt): #rysowanie wykresow predkosci cial w zaleznosci od czasu
        '''
        na razie generuje osobne wykresy dla kazdego ciala ale docelowo chce tak dobrac
        warunki poczatkowe, zeby ladnie wygladalo zestawienie wszystkich na jednym wykresie
        '''
        ox = np.linspace(0, N*dt, N+1)
        plt.subplot(1, 3, 1)
        plt.plot(ox, Body.vec_len(body1.v))
        plt.title('predkosci od czasu')
        plt.subplot(1, 3, 2)
        plt.plot(ox, Body.vec_len(body2.v))
        plt.subplot(1, 3, 3)
        plt.plot(ox, Body.vec_len(body3.v))
        plt.show()

if __name__=='__main__':
    #warunki poczatkowe
    
    #wersja z losowaniem:
    body1 = Body(10.0, np.random.rand(3)*4-2, np.random.rand(3)*20-10, np.array([0., 0., 0.]))
    body2 = Body(10.0, np.random.rand(3)*4-2, np.random.rand(3)*20-10, np.array([0., 0., 0.]))
    body3 = Body(10.0, np.random.rand(3)*4-2, np.random.rand(3)*20-10, np.array([0., 0., 0.]))
    '''
    #wersja z tak dobranymi liczbami, ze dla N i dt podanych ponizej wykresy sa choc troche ciekawsze niz zazwyczaj
    body1 = Body(10.0, np.array([0.80409107, 0.06872809, 0.43859513]), np.array([-2.19646316, 3.10772399, 2.2218612]), np.array([0., 0., 0.]))
    body2 = Body(10.0, np.array([0.06174344, 0.83440988, 0.22424054]), np.array([-2.44907015, 2.40024652, 4.2072139]), np.array([0., 0., 0.]))
    body3 = Body(10.0, np.array([0.12454915, 0.57659637, 0.12786532]), np.array([-5.95282591, 5.16875285, -8.95628201]), np.array([0., 0., 0.]))
    '''
    N = 1000 
    #N = np.random.randint(10, 10000) #do wyboru wersja z losowym N
    dt = 0.001 
    #dt = np.random.random()*0.003 + 0.0001 #do wyboru wersja z losowym krokiem czasowym
    
    Simulation.run(N, dt)
    print('Przemieszczenie srodka masy: od', Body.mcpos[0], 'do', Body.mcpos[-1])
    Simulation.v_plot(N, dt)

    
    print('1. cialo: polozenie poczatkowe:', body1.pos[0], 'predkosc poczatkowa:', body1.v[0])
    print('2. cialo: polozenie poczatkowe:', body2.pos[0], 'predkosc poczatkowa:', body2.v[0])
    print('3. cialo: polozenie poczatkowe:', body3.pos[0], 'predkosc poczatkowa:', body3.v[0])
    plt.subplot(1, 3, 1)
    plt.title('odleglosci od punktu (0,0) od czasu')
    body1.track()
    plt.subplot(1, 3, 2)
    body2.track()
    plt.subplot(1, 3, 3)
    body3.track()
    plt.show()
    
    #interact(Simulation.run, N=(1, 100), dt=(1, 100)) #nie dziala, chyba przeszkadza mu wywolyanie funkcji spoza funkcji interaktywnej
    
    '''
    efekt koncowy mocno zalezy od warunkow poczatkowych,
    a tu jest wyzwanie z sensownym ich dobraniem.
    '''
