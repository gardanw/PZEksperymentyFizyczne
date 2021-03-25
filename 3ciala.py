class Body:
    g = 6.6743 * 10**(-11)
    def __init__(self, mass, pos, v, a): # zdefiniowanie masy, pozycji, predkosci, przyspiesznia
        self.mass = mass
        self.pos = pos
        self.v = v
        self.a = a

    def move(self, dt): #dodaje do listy polozen kolejne polozenie
        for i in range(3):
            self.pos[i] += self.v[i]*dt + self.a[i]*dt*dt/2
            self.v[i] += self.a[i]*dt
        track1 += [self.pos]
        
    def update_acc(self, obj1, obj2): #do zmiany
        for i in range(3):
            if self.pos[i]-obj1.pos[i] != 0 and self.pos[i]-obj2.pos[i] != 0:
                self.a[i] = self.g*(obj1.mass/(self.pos[i]-obj1.pos[i])**2 + obj2.mass/(self.pos[i]-obj2.pos[i])**2)
            if self.pos[i]-obj1.pos[i] == 0 and self.pos[i]-obj2.pos[i] != 0:
                self.a[i] = self.g*(obj2.mass/(self.pos[i]-obj2.pos[i])**2)
            if self.pos[i]-obj1.pos[i] != 0 and self.pos[i]-obj2.pos[i] == 0:
                self.a[i] = self.g*(obj1.mass/(self.pos[i]-obj1.pos[i])**2)
            if self.pos[i]-obj1.pos[i] == 0 and self.pos[i]-obj2.pos[i] == 0:
                self.a[i] = 0.
    def leapfrog(self, dt): #dziala:)
        for i in range(3):
            self.pos[i] += self.v[i]*dt + self.a[i]*dt*dt/2
            self.v[i] = self.v[i] + self.a[i]*dt
    

body1 = Body(1, [0., 0., 0.], [1., 2., 1.], [0., 0., 0.])
body2 = Body(1, [5., 5., 5.], [0., 0., 0.], [0., 0., 0.])
body3 = Body(1, [8., 0., 3.], [0., 0., 0.], [0., 0., 0.])


track = body1.move(0.01, 5)
print(track)

#body1.update_acc(body2, body3)
#body1.leapfrog(0.1)
#print(body1.pos, body1.v, body1.a)
