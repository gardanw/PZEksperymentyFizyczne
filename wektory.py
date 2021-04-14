import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact

def W(działanie,A_x,A_y,B_x,B_y,C_x,C_y,D_x,D_y):
  A=[A_x,A_y]
  B=[B_x,B_y]
  C=[C_x,C_y]
  D=[D_x,D_y]
  E=[A_x,A_y]#PUNKT ZACZEPIENIA WEKTORA WYNIKOWEGO
  E_x=A_x
  E_y=A_y
  da=round(((np.abs(B_x-A_x))**2+(np.abs(B_y-A_y))**2)**(1/2),2) #długości wektorów
  db=round(((np.abs(D_x-C_x))**2+(np.abs(D_y-C_y))**2)**(1/2),2)
  print('współrzędne wektora a: punkt zaczepienia=',A,', punkt końcowy=',B)
  print('współrzędne wektora b: punkt zaczepienia=',C,', punkt końcowy=',D)
  print('długość wektora a=',da)
  print('długość wektora b=',db)

  fig=plt.figure(figsize=(13,10),dpi=100)
  plt.subplot(2,1,1)
  plt.plot(A_x,A_y,'o',color='orange')
  plt.plot(B_x,B_y)
  plt.quiver(A_x,A_y,B_x-A_x,B_y-A_y,angles='xy', scale_units='xy', scale=1,color='blue',label='wektor a (A,B)')
  plt.plot(C_x,C_y,'o',color='blue')
  plt.plot(D_x,D_y)
  plt.quiver(C_x,C_y,D_x-C_x,D_y-C_y,angles='xy', scale_units='xy', scale=1,color='red',label='wektor b (C,D)')
  plt.legend()
  plt.grid()

  def rownanie(A_x,A_y,B_x,B_y,C_x,C_y,D_x,D_y,E_x,E_y,F_x,F_y):
    E=[E_x,E_y]
    F=[F_x,F_y]
    print('c: punkt zaczepienia=',E,'punkt końcowy=',F)
    print('długość wektora c=',round(((np.abs(E_x-F_x))**2+(np.abs(E_y-F_y))**2)**(1/2),2))
    fig=plt.figure(figsize=(13,10),dpi=100)
    plt.subplot(2,1,2)
    plt.plot(A_x,A_y,'o')
    plt.plot(B_x,B_y)
    plt.quiver(A_x,A_y,B_x-A_x,B_y-A_y,angles='xy', scale_units='xy', scale=1,color='blue',label='wektor a (A,B)')
    plt.plot(C_x,C_y,'o')
    plt.plot(D_x,D_y)
    plt.quiver(C_x,C_y,D_x-C_x,D_y-C_y,angles='xy', scale_units='xy', scale=1,color='red',label='wektor b (C,D)')
    plt.plot(E_x,E_y)
    plt.plot(F_x,F_y)
    plt.quiver(E_x,E_y,F_x-E_x,F_y-E_y,angles='xy', scale_units='xy', scale=1,color='yellow',label='wektor c (E,F)')
    plt.plot([B_x,F_x],[B_y,F_y],'--')
    plt.plot([D_x,F_x],[D_y,F_y],'--')
    plt.legend()
    plt.grid()
    plt.show()

  if działanie=='dodawanie: a+b=c':
    D_x=A_x+D_x-C_x
    D_y=A_y+D_y-C_y
    C_x=A_x
    C_y=A_y
    F_x=B_x+D_x-A_x
    F_y=B_y+D_y-A_y
    rownanie(A_x,A_y,B_x,B_y,C_x,C_y,D_x,D_y,E_x,E_y,F_x,F_y)
  elif działanie=='odejmowanie: a-b=c':
    D_x=A_x+D_x-C_x
    D_y=A_y+D_y-C_y
    C_x=A_x
    C_y=A_y
    F_x=B_x-D_x+A_x
    F_y=B_y-D_y+A_y
    rownanie(A_x,A_y,B_x,B_y,C_x,C_y,D_x,D_y,E_x,E_y,F_x,F_y)
  else:
    F_x=B_x*D_x
    F_y=B_y*D_y
    print('Iloczyn skalarny:', F_x+F_y)

interact(W, działanie=['dodawanie: a+b=c','odejmowanie: a-b=c','iloczyn skalarny: a*b=c'],A_x=(0,10),A_y=(0,11),B_x=(0,11),B_y=(0,12),C_x=(0,12),C_y=(0,13),D_x=(0,13),D_y=(0,14))