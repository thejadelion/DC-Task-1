import random
import math
y = []
y1 = []
for i in range(100):
    y1.append(random.random())
for i in range(100):
    k = random.random()
    if k >0.5:
        y.append(1)
    else:
        y.append(0)

o = 0
for i in range(100):
    o += y[i]*math.log(y1[i])/math.log(2) + (1-y[i])*math.log(1-y1[i])/math.log(2)
o = o/(-100)
print(o)
