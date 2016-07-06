import numpy as np
import matplotlib.pyplot as plt
import math


# A simple seismic imaging exercise in python

# figure 1
fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(111)

#Where is the surface?
surface = (0) # always zero?
#Where is the origin?
origin = (0) # always zero?
#What is the offset?
offset = 20 # graph units

# Set out the seismic experiment equipment
source = origin + 10
receiver = source + offset
# Where is the mid-point?
mid = offset / 2 + source

# The basic geometry
# d = Vt/2
# Then, add a dipping reflector by connecting points that go to the right by two squares and vertically down by 1 square
right = 2
down = 1
# This creates an angle of tan-1(1/2) = 26.6*
dipReflect = math.degrees(math.atan(down/right))

yDR = np.linspace(0,receiver+5, num=receiver+6)
xDR = -1 * (yDR * math.tan(math.radians(dipReflect)))
#yDR_len = int(yDR[-1])
#xDR_len = int(xDR[-1])

#print(dipReflect, xDR, yDR, xDR_len, yDR_len)

ax.plot(yDR, xDR, color='black')
ax.xaxis.set_ticks([i for i in range(0,int(yDR[-1]))])
ax.yaxis.set_ticks([i for i in range(int(xDR[-1]),0)])
ax.grid(True)

# Next, put a source (labeled S) 10 units to the right of the origin
ax.plot([source], [surface], marker='o', color='b')
ax.text(source+3, surface+1, s='S=Shot', alpha=1.0, ha='right', va='center',
            fontsize=14, color='b')

# and a reciever (labeled R) 20 units to the right of the source
ax.plot([receiver], [surface], marker='o', color='r')
ax.text(receiver+5, surface+1, s='R=Receiver', alpha=1.0, ha='right', va='center',
            fontsize=14, color='r')

# label the midpoint (half way between the S and R equals M)
ax.plot([mid], [surface], marker='o', color='g')
ax.text(mid+5, surface+1, s='M=Midpoint', alpha=1.0, ha='right', va='center',
            fontsize=14, color='g')

# Mark the origin
ax.plot([origin], [surface], marker='o', color='black')
ax.text(origin+1, origin+1, s='O=0', alpha=1.0, ha='right', va='center',
            fontsize=14,)

# Add final annotation to match paper - figure 1
ax.text(source/2, surface + 0.4, s='Surface', alpha=1.0, ha='right', va='center',
            fontsize=14)
ax.text(mid, int(xDR[-1])/2 + 1, s='Dipping Reflector', alpha=1.0, ha='right', va='center',
            fontsize=14, rotation=360-dipReflect)

# Show Figure 1
#plt.show()

# start Figure 2

trueReflec1 = math.degrees(math.atan(right/down))
lengthTR1 = (math.cos(math.radians(trueReflec1)) * source) * 2

surfaceOffset = math.cos(math.radians(trueReflec1)) * lengthTR1
depthOffset = math.sin(math.radians(trueReflec1)) * lengthTR1 * -1
#print(lengthTR1, trueReflec1, surfaceOffset, depthOffset)

# use a dictionary for these points ... - go back and change?
sPrime = {'y':surfaceOffset, 'x':depthOffset}

ax.plot([sPrime['y']],[sPrime['x']], marker='o', color='black')
ax.text(surfaceOffset, depthOffset-1, s='S\'', alpha=1.0, ha='right', va='center',
            fontsize=14,)

yTR = np.linspace(source, surfaceOffset, num=surfaceOffset+1)
xTR = np.linspace(surface, depthOffset, num=surfaceOffset+1)

#print(yTR, xTR)
ax.plot(yTR, xTR, color='black')
#plt.show()

ySR = np.linspace(receiver, surfaceOffset, num=offset+surfaceOffset)
xSR = np.linspace(surface, depthOffset, num=offset+surfaceOffset)
ax.plot(ySR, xSR, color='black')
plt.show()