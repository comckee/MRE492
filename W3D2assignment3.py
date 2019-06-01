#Cole McKee
from matplotlib.pyplot import *
from numpy import *
t = arange(0,1,.01)
y = 2*sin(2*pi*t)
N = len(y)
y_sat = zeros(N)
 
for i in range(N):
     y_i = y[i]
     if y_i > 1.5:
         y_sat[i] = 1.5
     elif y_i < -1.5:
         y_sat[i] = -1.5
     else:
         y_sat[i] = y_i

figure(1)
clf()
xlabel('Time(sec.)')
ylabel('y(t)')         
plot(t,y_sat)

for i,y_i in enumerate(y):
     if y_i > 1.5:
         y_sat[i] = 1.5
     elif y_i < -1.5:
         y_sat[i] = -1.5
     else:
         y_sat[i] = y_i
         
figure(2)
clf()
xlabel('Time(sec.)')
ylabel('y(t)')         
plot(t,y_sat)


import copy
y_sat = copy.copy(y)

y_sat[y_sat > 1.5] = 1.5
y_sat[y_sat < -1.5] = -1.5

figure(3)
clf()
xlabel('Time(sec.)')
ylabel('y(t)')         
plot(t,y_sat)

inds1 = where(y > 1.5)[0]
y_sat[inds1] = 1.5
inds2 = where(y < -1.5)[0]
y_sat[inds2] = -1.5

figure(4)
clf()
xlabel('Time(sec.)')
ylabel('y(t)')         
plot(t,y_sat)