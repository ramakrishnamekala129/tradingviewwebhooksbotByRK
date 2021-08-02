
import numpy as np

import matplotlib.pyplot as plot
time        = np.arange(0, 10, 0.1);
amplitude   = np.sin(time)
plot.plot(time, amplitude)
plot.title('Sine wave')
plot.xlabel('Time')
plot.ylabel('Amplitude = sin(time)')
plot.grid(True, which='both')
plot.axhline(y=0, color='k')
plot.show()
plot.show()

import numpy as np
from matplotlib import pyplot as plt

h = [1,2,3,3,2]

x = [1,2,3,4,5]

N1 = len(x)
N2 = len(h)
N = N1+N2-1
y = np.zeros(N)
m = N-N1
n = N-N2
x =np.pad(x,(0,m),'constant')
h =np.pad(h,(0,n),'constant')
for n in range (N):
    for k in range (N):
        if n >= k:
             y[n] = y[n]+x[n-k]*h[k]


print('Linear convolution using convolution sum formula output response y =\n',y)


from scipy import array, zeros, signal
from scipy.fftpack import fft, ifft, convolve
def convfft(f, g):

  F = fft(f)
  G = fft(g)
  C = F * G
  c = ifft(C)

  return c