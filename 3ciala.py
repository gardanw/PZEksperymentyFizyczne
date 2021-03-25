class Body:
    g = 6.6743 * 10**(-11)
    def __init__(self, mass, pos, v, a): # zdefiniowanie masy, pozycji, predkosci, przyspiesznia
        self.mass = mass
        self.pos = [pos]
        self.v = v
        self.a = a

    def move(self, dt): #dodaje do listy polozen kolejne polozenie
        temp = self.pos[-1][:]
        for i in range(3):
            temp[i] += self.v[i]*dt + self.a[i]*dt*dt/2
            self.v[i] += self.a[i]*dt
        self.pos.append(temp)
        
    def update_acc(self, obj1, obj2): #przyspieszenie jednego ciala w zaleznosci od polozenia wzgl dwoch pozostalych
        for i in range(3):
            if self.pos[-1][i]-obj1.pos[-1][i] == 0 and self.pos[-1][i]-obj2.pos[-1][i] == 0:
                self.a[i] = 0.
            else: self.a[i] = self.g*(obj1.mass*(self.pos[-1][i]-obj1.pos[-1][i])/Body.vec_len(self.pos[-1], obj1.pos[-1]) + obj2.mass*(self.pos[-1][i]-obj2.pos[-1][i])/Body.vec_len(self.pos[-1], obj2.pos[-1]))

    def vec_len(v1, v2): #dlugosc wektora podniesiona do 3 potegi
        return ((v1[0]-v2[0])**2 + (v1[1]-v2[1])**2 + (v1[2]-v2[2])**2)**(3/2)
    
    def leapfrog(self, dt): #dziala, chwilowo niepotrzebne
        for i in range(3):
            self.pos[i] += self.v[i]*dt + self.a[i]*dt*dt/2
            self.v[i] = self.v[i] + self.a[i]*dt
    

body1 = Body(1, [0., 0., 0.], [1., 2., 1.], [0., 0., 0.])
body2 = Body(1, [5., 5., 5.], [0., 0., 0.], [0., 0., 0.])
body3 = Body(1, [8., 0., 3.], [0., 0., 0.], [0., 0., 0.])


body1.move(0.01)
body1.update_acc(body2, body3)
print(body1.a)
