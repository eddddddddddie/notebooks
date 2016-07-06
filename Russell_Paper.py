import numpy as np
import matplotlib.pyplot as plt
import math

# A simple seismic imaging exercise in python

# figure 1
fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(111)

# The basic geometry
# d = Vt/2
# This creates an angle of tan-1(1/2) = 26.6*
dipReflect = math.degrees(math.atan(1/2))

y = np.linspace(0,35, num=36)
x = -1 * (y * math.tan(math.radians(dipReflect)))
#y_len = int(y[-1])
#x_len = int(x[-1])

#print(dipReflect, x, y, x_len, y_len)

ax.plot(y, x, color='black')
ax.xaxis.set_ticks([i for i in range(0,int(y[-1]))])
ax.yaxis.set_ticks([i for i in range(int(x[-1]),0)])
ax.grid(True)

# Mark the origin
ax.plot([0], [0], marker='o')
ax.text(1, 0.5, s='O=0', alpha=1.0, ha='right', va='center',
            fontsize=14,)

#Where is the surface?
surface = 0
#Where is the origin?
origin = 0
# Set out the seismic experiment equipment
source = origin + 10
receiver = source + 20
# Where is the mid-point?
mid = receiver - source

# Next, put a source (labeled S) 10 units to the right of the origin
ax.plot([source], [surface], marker='o', color='b')
ax.text(source+3, surface+0.5, s='S=Shot', alpha=1.0, ha='right', va='center',
            fontsize=14, color='b')

# and a reciever (labeled R) 20 units to the right of the source
ax.plot([receiver], [surface], marker='o', color='r')
ax.text(receiver+5, surface+0.5, s='R=Receiver', alpha=1.0, ha='right', va='center',
            fontsize=14, color='r')

# label the midpoint (half way between the S and R equals M)
ax.plot([mid], [surface], marker='o', color='g')
ax.text(mid+5, surface+0.5, s='M=Midpoint', alpha=1.0, ha='right', va='center',
            fontsize=14, color='g')

# Mark the origin
ax.plot([origin], [surface], marker='o', color='black')

# Add final annotation to match paper
ax.text(origin+5, surface+0.4, s='Surface', alpha=1.0, ha='right', va='center',
            fontsize=14)
ax.text(origin+22, surface-8.5, s='Dipping Reflector', alpha=1.0, ha='right', va='center',
            fontsize=14, rotation=360-dipReflect)

# Show Figure 1
plt.show()
