import sys
import math
import time
import random
import numpy as np
import matplotlib.pyplot as plt


#calculate the distance between two points
def distance(p1, p2):
    global count
    count+=1
    dis = 0
    for i in range(len(p1)):
        dis += (p1[i] - p2[i]) ** 2
    return math.sqrt(dis)

def shortest_distance(points):
    
    #even number of points base
    if len(points) == 2:
        return distance(points[0], points[1]), points[0], points[1]
    #odd number of points base
    elif len(points) == 3:
        min_distance = rand
        point1 = points[0]
        point2 = points[1]
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                dis = distance(points[i], points[j])
                if dis < min_distance:
                    min_distance = dis
                    point1 = points[i]
                    point2 = points[j]
        return min_distance, point1, point2
    else:
        mid = len(points) // 2
        left_min_distance, left_point1, left_point2 = shortest_distance(points[:mid])
        right_min_distance, right_point1, right_point2 = shortest_distance(points[mid:])
        if left_min_distance < right_min_distance:
            min_distance = left_min_distance
            point1 = left_point1
            point2 = left_point2
        else:
            min_distance = right_min_distance
            point1 = right_point1
            point2 = right_point2
        mid_x = points[mid][0]
        mid_points = []
        for point in points:
            if abs(point[0] - mid_x) < min_distance:
                mid_points.append(point)
        for i in range(len(mid_points)):
            for j in range(i+1, len(mid_points)):
                dis = distance(mid_points[i], mid_points[j])
                if dis < min_distance:
                    min_distance = dis
                    point1 = mid_points[i]
                    point2 = mid_points[j]
        
        return min_distance, point1, point2

def main():
    global count
    global rand
    n = int(input('Please input the number of points: '))
    d = int(input('Please input the dimension of points: '))
    #generate random points
    points = []
    for i in range(n):
        point = []
        for j in range(d):
            point.append(random.randint(0, rand))
        points.append(point)
    start = time.time()
    points = sorted(points, key=lambda point: point[0])
    #calculate the shortest distance
    min_distance, point1, point2= shortest_distance(points)
    end = time.time()
    print('The shortest distance is: ', min_distance)
    print('The two points are: ', point1, point2)
    print('The time cost is: ', end - start)
    print('Euclidian count: ', count)

    #plot the points
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
    else:
        print("Cannot be plotted!")

    plt.show()

if __name__ == '__main__':
    count = 0
    rand = 1000
    main()