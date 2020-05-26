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
fig, axes = plt.subplots(nrows=2, ncols=3)
# Save the graph as png
fig.savefig("plot.png", dpi=200)

# to show the plot
plt.show()
