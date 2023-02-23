import sys
import math
import time
import random
import numpy as np
import matplotlib.pyplot as plt

#divide and conquer algorithm
def divide_and_conquer(points):
    if len(points) == 1:
        return points
    elif len(points) == 2:
        return points
    else:
        mid = len(points) // 2
        left = divide_and_conquer(points[:mid])
        right = divide_and_conquer(points[mid:])
        return merge(left, right)

#merge two list
def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

#calculate the distance between two points
def distance(p1, p2):
    dis = 0
    for i in range(len(p1)):
        dis += (p1[i] - p2[i]) ** 2
    return math.sqrt(dis)

#calculate the shortest distance between two points
def shortest_distance(points):
    min_distance = distance(points[0], points[1])
    point1 = points[0]
    point2 = points[1]
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            if distance(points[i], points[j]) <= min_distance:
                min_distance = distance(points[i], points[j])
                point1 = points[i]
                point2 = points[j]
    return min_distance, point1, point2

def main():
    #input the number of points
    n = int(input('Please input the number of points: '))
    #input the dimension of points
    d = int(input('Please input the dimension of points: '))
    #generate random points
    points = []
    for i in range(n):
        point = []
        for j in range(d):
            point.append(random.randint(0, 200))
        points.append(point)
    start = time.time()
    #sort the points by x
    points = divide_and_conquer(points)
    #calculate the shortest distance
    min_distance, point1, point2 = shortest_distance(points)
    end = time.time()
    print('The shortest distance is: ', min_distance)
    print('The two points are: ', point1, point2)
    print('The time cost is: ', end - start)
    print(points)
    #plot the points
    x = []
    y = []
    z = []
    c = []
    s = []
    o = [] 
    for point in points:
        x.append(point[0])
        y.append(point[1])
        z.append(point[2])
        if len(point) >= 4:
            c.append(point[3])
        if len(point) >= 5:
            s.append(point[4])

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    if len(point) == 3:
        x.remove(point1[0])
        x.remove(point2[0])
        y.remove(point1[1])
        y.remove(point2[1])
        z.remove(point1[2])
        z.remove(point2[2])
        ax.scatter(x, y, z, c='black')
        ax.scatter(point1[0], point1[1], point1[2], c='blue')
        ax.scatter(point2[0], point2[1], point2[2], c='blue')
    if len(point) == 4:
        img = ax.scatter(x, y, z, c=c, cmap=plt.hot())
        fig.colorbar(img)
    if len(point) == 5:
        img = ax.scatter(x, y, z, c=c, cmap=plt.hot(), s=s)
        fig.colorbar(img)

    x_line = [point1[0], point2[0]]
    y_line = [point1[1], point2[1]]
    z_line = [point1[2], point2[2]]
    ax.plot(x_line, y_line, z_line, c='blue')


    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()

if __name__ == '__main__':
    main()