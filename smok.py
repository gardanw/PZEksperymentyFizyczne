from numpy import zeros, arange
from numpy.random import randint
import matplotlib.pyplot as plt
from ipywidgets import interact
def Smok(N):
  def smok(N):
    Punkty = zeros((N, 2))
    r = randint(2, size=N)
    for k in arange(1, N):
      if r[k]:
        Punkty[k] = -0.4 * Punkty[k - 1] + [-1., .1]
      else:
        Punkty[k] = .76 * Punkty[k - 1] + [-.4, .4] * Punkty[k - 1][::-1]
    return Punkty

  Punkty = smok(N)[100:]
  plt.plot(Punkty[:, 0], Punkty[:, 1], ',')
  plt.title('Smok dla N = {}'.format(N))
  plt.show()
interact(Smok, N = (100,100000,10))