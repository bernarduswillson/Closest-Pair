import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
import math
 
#plot the points
def plot(points, point1, point2, rand):
    x = []
    y = []
    z = []
    c = []
    s = []
    o = [] 
    for point in points:
        if len(point) >= 1:
            x.append(point[0])
        if len(point) >= 2:
            y.append(point[1])
        if len(point) >= 3:
            z.append(point[2])
        if len(point) >= 4:
            c.append(point[3])
        if len(point) >= 5:
            s.append(point[4])
        if len(point) >= 6:
            o.append(point[5]*(1/rand))

    fig = plt.figure()
    if len(point) <= 2:
        if len(point) == 1:
            y = [0] * len(x)
            plt.scatter(x, y, c='black', alpha=1)
            plt.scatter(point1[0], 0, c='blue')
            plt.scatter(point2[0], 0, c='blue')
            x_line = [point1[0], point2[0]]
            y_line = [0, 0]
            plt.plot(x_line, y_line)
        if len(point) == 2:
            plt.scatter(x, y, c='black', alpha=1)
            plt.scatter(point1[0], point1[1], c='blue')
            plt.scatter(point2[0], point2[1], c='blue')
            x_line = [point1[0], point2[0]]
            y_line = [point1[1], point2[1]]
            plt.plot(x_line, y_line)
        plt.show()
    elif len(point) <= 6:
        ax = fig.add_subplot(111, projection='3d')
        if len(point) == 3:
            x.remove(point1[0])
            x.remove(point2[0])
            y.remove(point1[1])
            y.remove(point2[1])
            z.remove(point1[2])
            z.remove(point2[2])
            ax.scatter(x, y, z, c='black', alpha=1)
            ax.scatter(point1[0], point1[1], point1[2], c='blue')
            ax.scatter(point2[0], point2[1], point2[2], c='blue')
        if len(point) == 4:
            img = ax.scatter(x, y, z, c=c, cmap=plt.hot(), alpha=1)
            fig.colorbar(img)
        if len(point) == 5:
            img = ax.scatter(x, y, z, c=c, cmap=plt.hot(), s=s, alpha=1)
            fig.colorbar(img)
        if len(point) == 6:
            img = ax.scatter(x, y, z, c=c, cmap=plt.hot(), s=s, alpha=o)
            fig.colorbar(img)

        x_line = [point1[0], point2[0]]
        y_line = [point1[1], point2[1]]
        z_line = [point1[2], point2[2]]
        ax.plot(x_line, y_line, z_line, c='blue')
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')
        plt.show()
    else:
        print("\nTidak dapat divisualisasikan!")