import numpy as np

class Body:
    g = 6.6743 * 10**(-11)
    def __init__(self, mass, pos, v, a):
        self.mass = mass
        self.pos = [pos] #lista 3elementowych tablic numpy, czyli caly przebyty tor
        self.v = v #3elementowa tablica numpy
        self.a = a #3elementowa tablica numpy

    def vec_len(v1, v2): #dlugosc wektora laczacego konce 2 wektorow podniesiona do 3 potegi
        return ((v1[0]-v2[0])**2 + (v1[1]-v2[1])**2 + (v1[2]-v2[2])**2)**(3/2)

    def leapfrog(self, dt, obj1, obj2): #dodaje nowe polozenie do listy, aktualizuje v, liczy a
        temp = self.pos[-1].copy()
        self.v += 0.5*self.a*dt
        self.pos.append(temp + self.v*dt)
        self.a = self.g*(obj1.mass*(obj1.pos[-1]-self.pos[-1])/Body.vec_len(self.pos[-1], obj1.pos[-1]) + obj2.mass*(obj2.pos[-1]-self.pos[-1])/Body.vec_len(self.pos[-1], obj2.pos[-1]))
        self.v += 0.5*self.a*dt 

#warunki poczatkowe
body1 = Body(10, np.array([0., 0., 0.]), np.array([1., 1., 0.3]), np.array([0., 0., 0.]))
body2 = Body(10, np.array([0.5, 1., 0.5]), np.array([0., -1., -0.5]), np.zeros(3))
body3 = Body(10, np.array([1., 0.5, 0.]), np.array([-0.5, -0.1, 0.]), np.zeros(3))

dt = 0.001 #krok czasowy
N = 10 #liczba powtorzen


for i in range(N): #generownie torow ruchu
    body1.leapfrog(dt, body2, body3)
    body2.leapfrog(dt, body1, body3)
    body3.leapfrog(dt, body1, body2)
print(body1.pos, body2.pos, body3.pos)
'''
efekt koncowy mocno zalezy od warunkow poczatkowych,
a tu jest wyzwanie z sensownym ich dobraniem.
'''
