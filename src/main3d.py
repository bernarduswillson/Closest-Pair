# shortest path 3d with divide and conquer algorithm

# Path: src/main3d.py
# Compare this snippet from src/main.py:
# # shortest path with divide and conquer algorithm
#
import sys
import math
import time
import random
import numpy as np
import matplotlib.pyplot as plt

#divide and conquer algorithm in 3d
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

#merge two sorted list
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
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)

#calculate the shortest distance between two points
def shortest_distance(points):
    min_distance = distance(points[0], points[1])
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            if distance(points[i], points[j]) < min_distance:
                min_distance = distance(points[i], points[j])
                point1 = points[i]
                point2 = points[j]
    return min_distance, point1, point2


def main():
    #input the number of points
    n = int(input('Please input the number of points: '))
    #generate n random points
    points = []
    for i in range(n):
        points.append([random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)])
    #sort the points by x coordinate
    points = divide_and_conquer(points)
    #calculate the shortest distance
    start = time.time()
    min_distance, point1, point2 = shortest_distance(points)
    end = time.time()
    print('The shortest distance is: ', min_distance)
    print('The two points are: ', point1, point2)
    print('The time cost is: ', end - start)
    #plot the points
    x = []
    y = []
    z = []
    for point in points:
        x.append(point[0])
        y.append(point[1])
        z.append(point[2])
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x.remove(point1[0])
    x.remove(point2[0])
    y.remove(point1[1])
    y.remove(point2[1])
    z.remove(point1[2])
    z.remove(point2[2])
    ax.scatter(x, y, z, c='black')
    ax.scatter(point1[0], point1[1], point1[2], c='red')
    ax.scatter(point2[0], point2[1], point2[2], c='red')

    x_line = [point1[0], point2[0]]
    y_line = [point1[1], point2[1]]
    z_line = [point1[2], point2[2]]
    ax.plot(x_line, y_line, z_line, c='red')


    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.show()

if __name__ == '__main__':
    main()