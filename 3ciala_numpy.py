import numpy as np
import matplotlib.pyplot as plt

class Body:
    g = 6.6743 * 10**(-11)
    def __init__(self, mass, pos, v, a):
        self.mass = mass
        self.pos = [pos] #lista 3elementowych tablic numpy, czyli caly przebyty tor
        self.v = [v] #lista 3elementowych tablic numpy, czyli cala historia predkosci
        self.a = a #3elementowa tablica numpy

    def difference_len(v1, v2): #dlugosc wektora laczacego konce 2 wektorow podniesiona do 3 potegi
        return ((v1[0]-v2[0])**2 + (v1[1]-v2[1])**2 + (v1[2]-v2[2])**2)**(3/2)

    def vec_len(v):
        vec_len_list = []
        for i in range(len(v)):
            vec_len_list.append(np.sqrt((v[i][0])**2 + (v[i][1])**2))
        return vec_len_list

    def leapfrog(self, dt, obj1, obj2): #dodaje nowe polozenie do listy, aktualizuje v, liczy a
        pos_temp = self.pos[-1].copy()
        v_temp = self.v[-1].copy()
        self.v.append(v_temp + 0.5*self.a*dt)
        self.pos.append(pos_temp + self.v[-1]*dt)
        self.a = self.g*(obj1.mass*(obj1.pos[-1]-self.pos[-1])/Body.difference_len(self.pos[-1], obj1.pos[-1]) + obj2.mass*(obj2.pos[-1]-self.pos[-1])/Body.difference_len(self.pos[-1], obj2.pos[-1]))
        self.v[-1] += 0.5*self.a*dt 

class Simulation:
    def run(N, dt): #generowanie torow ruchu dla podanych liczby powtorzen i kroku czasowego
        for i in range(N):
            body1.leapfrog(dt, body2, body3)
            body2.leapfrog(dt, body1, body3)
            body3.leapfrog(dt, body1, body2)
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
        ox = np.arange(0, N*dt+dt, dt)
        plt.subplot(1, 3, 1)
        plt.plot(ox, Body.vec_len(body1.v))
        plt.subplot(1, 3, 2)
        plt.plot(ox, Body.vec_len(body2.v))
        plt.subplot(1, 3, 3)
        plt.plot(ox, Body.vec_len(body3.v))
        plt.show()

if __name__=='__main__':
    #warunki poczatkowe
    body1 = Body(100, np.array([0., 0., 0.]), np.array([1., 1., 0.3]), np.array([0., 0., 0.]))
    body2 = Body(100, np.array([0.5, 1., 0.5]), np.array([-2., -2., -0.5]), np.array([0., 0., 0.]))
    body3 = Body(100, np.array([1., 0.5, 0.]), np.array([-4., 0., 0.]), np.array([0., 0., 0.]))

    Simulation.run(1000, 0.001)
    Simulation.v_plot(1000, 0.001)
    
'''
efekt koncowy mocno zalezy od warunkow poczatkowych,
a tu jest wyzwanie z sensownym ich dobraniem.
'''
