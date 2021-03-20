import numpy as np
from ipywidgets import interact
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.linalg import norm

def atom_tf(ro ,L ,A):
  r=(A/np.pi)**(1/2)
  print('Opór właściwy (ro)=',np.round(ro,2),'Om*m')
  print('Długość przewodnika (L)=',np.round(L,2),'m')
  print('Pole przekroju poprzecznego przewodnika (A)=',np.round(A,2),'m^2')
  print('Opór elektryczny(R)=',np.round((ro*L)/A,2),'Om')

  fig = plt.figure(figsize=(10,8))
  ax = fig.add_subplot(111, projection='3d')
  origin = np.array([0, 0, 0])
  
  p0 = np.array([1, 3, 2])
  p1 = np.array([8, 5, 9])
  R = r
  
  v = p1 - p0
  mag = norm(v)
  v = v / mag
  not_v = np.array([1, 0, 0])
  if (v == not_v).all():
      not_v = np.array([0, 1, 0])
  
  n1 = np.cross(v, not_v)
  n1 /= norm(n1)
  n2 = np.cross(v, n1)
  t = np.linspace(0, L, 100)
  theta = np.linspace(0, 2 * np.pi, 100)
  t, theta = np.meshgrid(t, theta)
  
  X, Y, Z = [p0[i] + v[i] * t + R * np.sin(theta) * n1[i] + R * np.cos(theta) * n2[i] for i in [0, 1, 2]]
  ax.plot_surface(X, Y, Z,color='yellow')
  
  ax.set_xlim(0, 15)
  ax.set_ylim(0, 10)
  ax.set_zlim(0, 15)
  plt.show()
interact(atom_tf, ro = (0.01,1.0,0.01),L = (0.1,20.0,0.11), A =(0.01,15.0,0.6))
