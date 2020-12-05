import numpy as np
import matplotlib.pyplot as plt
import random
import matplotlib.animation as animation
import time

t1 = time.time()
'''Creatin the Square-lattice with random spins'''
n = 50     #size of lattice
s = np.zeros((n, n))
for i in range(n):
      for j in range(n):
            r = random.random()
            if r < .5:
                  s[i][j] = 1
            else:
                  s[i][j] = -1
#print(s)

'''Ploting the Square-lattice with random spins (Unaligned)'''
#plt.imshow(s)
#plt.show()

'''Functions for the energies'''
def E1(i, j):
      return -s[i][j]*(s[(i+1)%n][j]+s[(i-1)%n][j]+s[i][(j+1)%n]+s[i][(j-1)%n])
def E2(i, j):
      return -E1(i, j)


def ising():
      for l in range(n**2):
            i = random.randint(0, n-1)
            j = random.randint(0, n-1)
            
            e1 = E1(i, j)
            e2 = E2(i, j)
            de = e2-e1
                  
            if de < 0 or random.random() < np.exp(-de/.1):
                        s[i][j] *= -1
      return s

'''Animating the evolution'''
ims = []
fig = plt.figure()
for k in range(500):
      im = plt.imshow(ising(), animated=True)
      ims.append([im])



ani = animation.ArtistAnimation(fig, ims, interval=200, blit=True,
                                repeat_delay=1000)

t2 = time.time()
print('Duration = ', t2-t1)
plt.title('Animation')
plt.show()

'''Saving the animation'''
'''
t1 = time.time()
ani.save('animation.mp4', dpi = 300)
t2 = time.time()
print('Duration = ', t2-t1)
'''
