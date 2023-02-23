# shortest path with divide and conquer algorithm

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
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

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
        points.append([random.randint(0, 100), random.randint(0, 100)])
    print(points)

    #sort the points by x coordinate
    points = divide_and_conquer(points)

    #calculate the shortest distance
    start = time.time()
    min_distance, point1, point2 = shortest_distance(points)
    end = time.time()
    print(point1, point2)
    #display with matplotlib, show the closest point with red color
    x = []
    y = []
    for i in range(len(points)):
        x.append(points[i][0])
        y.append(points[i][1])
    plt.scatter(x, y, c='b')
    plt.scatter(point1[0], point1[1], c='r')
    plt.scatter(point2[0], point2[1], c='r')
    plt.show()

    print('The shortest distance is: %f' % min_distance)
    print('The running time is: %f' % (end - start))


main()