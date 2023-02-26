import math
import time
import random
import others.plot as plot
import platform


# calculate the distance between two points and count the number of distance calculation
def distance(p1, p2):
    global count
    count += 1
    dis = 0
    for i in range(len(p1)):
        dis += (p1[i] - p2[i]) ** 2
    return math.sqrt(dis)


# DnC quick sort the points
def quickSort(points):
    if len(points) <= 1:
        return points
    else:
        pivot = points[0]
        left = []
        right = []
        for i in range(1, len(points)):
            if points[i] < pivot:
                left.append(points[i])
            else:
                right.append(points[i])
        return quickSort(left) + [pivot] + quickSort(right)


# find the shortest distance between two points
def DnCShortestDistance(points):
    # even number of points base
    if len(points) == 2:
        return distance(points[0], points[1]), points[0], points[1]
    
    # odd number of points base, brute force
    elif len(points) == 3:
        minDistance = rand*rand
        point1 = points[0]
        point2 = points[1]
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                dis = distance(points[i], points[j])
                if dis < minDistance:
                    minDistance = dis
                    point1 = points[i]
                    point2 = points[j]
        return minDistance, point1, point2
    
    # recursive finding the shortest distance
    else:
        mid = len(points) // 2
        leftMinDistance, leftPoint1, leftPoint2 = DnCShortestDistance(points[:mid])
        rightMinDistance, rightPoint1, rightPoint2 = DnCShortestDistance(points[mid:])
        if leftMinDistance < rightMinDistance:
            minDistance = leftMinDistance
            point1 = leftPoint1
            point2 = leftPoint2
        else:
            minDistance = rightMinDistance
            point1 = rightPoint1
            point2 = rightPoint2

        # find the points that are close to mid point (strip)
        midPoint = points[mid][0]
        midPoints = []
        for i in range(len(points)):
            if midPoint - minDistance < points[i][0] < midPoint + minDistance:
                midPoints.append(points[i])

        # find the shortest distance between the points in mid points
        for i in range(len(midPoints)):
            for j in range(i+1, len(midPoints)):
                flag = True
                for k in range(len(midPoints[i])):
                    if abs(midPoints[i][k] - midPoints[j][k]) > minDistance:
                        flag = False
                if flag:
                    dis = distance(midPoints[i], midPoints[j])
                    if dis < minDistance:
                        minDistance = dis
                        point1 = midPoints[i]
                        point2 = midPoints[j]
        
        return minDistance, point1, point2


#brute force comparison
def BFShortestDistance(points):
    minDistance = rand * rand
    point1 = points[0]
    point2 = points[1]
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            dis = distance(points[i], points[j])
            if dis < minDistance:
                minDistance = dis
                point1 = points[i]
                point2 = points[j]
    return minDistance, point1, point2


def main():
    global count
    global rand

    # splash screen from txt file
    with open('src/others/splashScreen.txt', 'r') as file:
        contents = file.read()
        print(contents)

    # input validations
    flag = False
    while not flag:
        n = int(input('Masukkan jumlah titik: '))
        if n < 2:
            print('Jumlah titik minimal 2! Silahkan masukkan kembali.\n')
        else:
            flag = True
    flag = False
    while not flag:
        d = int(input('Masukkan jumlah dimensi: '))
        if d < 1:
            print('Jumlah dimensi minimal 1! Silahkan masukkan kembali.\n')
        else:
            flag = True

    # generate random points
    points = []
    for i in range(n):
        point = []
        for j in range(d):
            point.append(random.uniform(0, rand))
        points.append(point)


    # ~DIVIDE AND CONQUER~
    start = time.time()

    # sort the points based on x coordinate
    points = quickSort(points)

    # calculate the shortest distance
    minDistance, point1, point2 = DnCShortestDistance(points)
    end = time.time()
    print('--------------------------------------------------------------------------------------------')
    print('~DIVIDE AND CONQUER~')
    print('Dua titik yang paling berdekatan:')
    print('Titik 1:',', '.join("{:.2f}".format(p) for p in point1))
    print('Titik 2:',', '.join("{:.2f}".format(p) for p in point2))
    print('\nJaraknya adalah: {:.2f}'.format(minDistance))
    print('Banyaknya operasi perhitungan rumus Euclidian: ', count)
    print('--------------------------------------------------------------------------------------------')
    print('Waktu eksekusi: {:.2f} ms'.format((end - start) * 1000))
    
    #plot the points
    plot.plot(points, point1, point2, rand)

    print('--------------------------------------------------------------------------------------------')
    print('--------------------------------------------------------------------------------------------')


    # ~BRUTE FORCE~
    count = 0
    start = time.time()

    # calculate the shortest distance
    minDistance, point1, point2 = BFShortestDistance(points)
    end = time.time()
    print('~BRUTE FORCE~')
    print('Dua titik yang paling berdekatan:')
    print('Titik 1:',', '.join("{:.2f}".format(p) for p in point1))
    print('Titik 2:',', '.join("{:.2f}".format(p) for p in point2))
    print('\nJaraknya adalah: {:.2f}'.format(minDistance))
    print('Banyaknya operasi perhitungan rumus Euclidian: ', count)
    print('--------------------------------------------------------------------------------------------')
    print('Waktu eksekusi: {:.2f} ms'.format((end - start) * 1000))
    print('--------------------------------------------------------------------------------------------')
    print(platform.processor())


if __name__ == '__main__':
    # euclidian distance counter
    count = 0
    # random number range
    rand = 1000.0
    main()