from matplotlib.pyplot import *
from numpy import *
t = arange(1,3,0.02)
y = 6*np.log(t) - 7*np.exp(0.2*t)
figure(1)
clf()
plot(t,y)
xlabel('Time (min)')
ylabel('Temperature (°C)')
title('McKee - Plot')
show()
print('Hello World! I just wrote my first Python program. Yayyyyyyy')
print('Cole McKee')