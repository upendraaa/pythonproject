import matplotlib.pyplot as plt;
import numpy as np;

x = np.arange(0, 100)
y = x * 2
z = x ** 2

# Question 1 plot x,y
# fig = plt.figure()
# axes = fig.add_axes([0.1,0.1,.8,.8])
# axes.plot(x,y)
# axes.set_xlabel("X")
# axes.set_ylabel("Y")
# axes.set_title("Title")

# Figure object with two subplots
# fig = plt.figure()
# ax1 = fig.add_axes([.1,.1,.8,.8])
# ax2 = fig.add_axes([.2,.5,.2,.2])
# ax1.plot(x,y,color = 'red')
# ax2.plot(x,y, color = 'r')
#
# ax1.set_xlabel("X")
# ax1.set_ylabel("Y")
# ax1.set_title("Title")

# Adding two axes in figure object
# fig = plt.figure()
# ax1 = fig.add_axes([.1,.1,.9,.9])
# ax2 = fig.add_axes([.2,.5,.4,.4])

# set limit in graph

# fig = plt.figure()
# ax1 = fig.add_axes([.1,.1,.8,.8])
# ax2 = fig.add_axes([.2,.5,.3,.3])
# ax1.plot(x,z)
# ax1.set_xlabel("X")
# ax1.set_ylabel("Z")
#
# ax2.plot(x,y)
# ax2.set_xlabel("X")
# ax2.set_ylabel("Y")
# ax2.set_xlim([20,22])
# ax2.set_ylim([30,50])

# Create the subplots
fig, axes = plt.subplots(nrows=1, ncols=2)

# for ax in axes:
#     ax.plot(x,y)

axes[0].plot(x, y)
axes[1].plot(x, z)

plt.show()
