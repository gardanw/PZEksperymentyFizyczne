# tor ruchu pocisku
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style as style
from ipywidgets import interact

def rzut(θ,v0):
  Δ = .01  # krok czasowy
  g = 9.81  # przyspieszenie ziemskie
  α = .05  # współczynnik siły oporu na jedn. masy

  def balistyczna(v0=v0, θ=θ, α=α, g=g, Δ=Δ):
      X = [0., Δ * v0 * np.cos(θ)]
      Y = [0., Δ * v0 * np.sin(θ)]
      k = 2
      while Y[-1] >= 0:
          X.append(((2 + α * Δ) * X[-1] - X[-2]) / (1 + α * Δ))
          Y.append(((2 + α * Δ) * Y[-1] - Y[-2] - g * Δ**2) / (1 + α * Δ))
          k += 1
      return X, Y

  def V(X, Y, Δ=Δ):
      return np.sqrt((X[1:] - X[:-1]) ** 2 + (Y[1:] - Y[:-1]) ** 2) / Δ

  if __name__ == '__main__':
      
      X, Y = balistyczna()
      style.use('seaborn-dark')
      fig, (ax1, ax2,ax3) = plt.subplots(3, 1)
      ax1.plot(X, Y)
      ax1.grid(True)
      ax1.set_title('Krzywa balistyczna (tor ruchu pocisku)')
      ax1.set_xlabel('odległość [m]')
      ax1.set_ylabel('wysokość [m]')
      k = len(X)
      ax1.legend((f'θ={round(θ/np.pi,2)}π, v0={v0}, α={α}, czas={k * Δ:.2f}',))
      X, Y = np.array(X), np.array(Y)
      ax2.set_title('Zależność prędkości od czasu')
      ax2.plot(Δ * np.arange(X.size - 1), V(X, Y))
      ax2.grid(True)
      ax2.legend(('prędkość pocisku',))
      ax2.set_xlabel('czas [s]')
      ax2.set_ylabel('prędkość [m/s]')
      
      ax3.set_title('Zależność wysokości od czasu')
      ax3.plot(Δ * np.arange(X.size),Y)
      ax3.grid(True)
      ax3.legend(('wysokość pocisku',))
      ax3.set_xlabel('czas [s]')
      ax3.set_ylabel('wysokość [m]')
      fig.tight_layout()
      plt.show()
      print('przyspieszenie ziemskie (g)=',g,'m/s^2')
      print('współczynnik siły oporu na jednostkę masy (α)=',α)
      print('kąt początkowy (θ)=',round(θ/np.pi,2),'π')
      print('prędkość początkowa (v0)=',v0,'m/s')
      print(f'czas lotu pocisku (t)={k * Δ:.2f} s')
interact(rzut, θ=(np.pi / 6, np.pi/2),v0 = (10,1800))