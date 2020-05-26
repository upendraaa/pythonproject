import matplotlib.pyplot as plt
import numpy as np

# 10 points between 0 to 20
x = np.linspace(0, 20, 10)
# Square of x
y = x ** 2

# plt.plot(x,y)


# To print lable
# plt.xlabel("X label")
# plt.ylabel("Y label")
# plt.title("Title")

# Subplot

# plt.subplot(1,2,1)
# plt.plot(x,y,'r')
# plt.show()

# plt.subplot(1,2,1)
# plt.plot(y,x,'b')
# plt.show()

# Add figure
# fig = plt.figure()
# axes = fig.add_axes([0.1,0.1,0.8,0.8])
# axes.plot(x,y)
# axes.set_xlabel("X Label figure")
# axes.set_ylabel("Y Label figure")

# Axis inside axis
# fig = plt.figure()
# axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
# axes2 = fig.add_axes([0.2,0.5,0.3,0.3])
# axes1.plot(x,y)
# axes2.plot(y,x)

# Figure subplots
# 2 rows and three column
# fig, axes = plt.subplots(nrows=2, ncols=3)
# Save the graph as png
# fig.savefig("plot.png", dpi=200)

# Axis test, show label and legends at given location
# fig = plt.figure()
# axes1 = fig.add_axes([0.1,0.1,.8,.8])
# axes1.plot(x,x**2,label = "Squared")
# axes1.plot(x,x**3, label = "cubed")
# axes1.plot(x,x**4, label ="Power 4")
# axes1.plot(x,x**5, label = "Power 5")
# axes1.plot(x,x**6, label = "Power 6")
# axes1.legend(loc = 0)
# fig.savefig("multipicatin_graph.png")

# Figure with color, alpha is show the transparency's level, and different style
fig = plt.figure()
axes = fig.add_axes([.1, .1, .8, .8])
axes.plot(x, y, color='red', linewidth=2, alpha=.5, linestyle="--", marker="o", markersize=10
          , markerfacecolor='yellow', markeredgewidth=3, markeredgecolor='green')
# plt.scatter(x,y)

# to show the plot
plt.show()
