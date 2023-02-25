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


# quick sort the points based on x coordinate
def sort(points):
    def quickSort(points, start, end):
        if start < end:
            pivot = partition(points, start, end)
            quickSort(points, start, pivot - 1)
            quickSort(points, pivot + 1, end)

    def partition(points, start, end):
        pivot = points[end][0]
        i = start - 1
        for j in range(start, end):
            if points[j][0] <= pivot:
                i += 1
                points[i], points[j] = points[j], points[i]
        points[i + 1], points[end] = points[end], points[i + 1]
        return i + 1

    quickSort(points, 0, len(points) - 1)
    return points


#find the shortest distance between two points
def shortest_distance(points):
    #even number of points base
    if len(points) == 2:
        return distance(points[0], points[1]), points[0], points[1]
    
    #odd number of points base
    elif len(points) == 3:
        minDistance = rand
        point1 = points[0]
        point2 = points[1]
        #brute force comparison
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                dis = distance(points[i], points[j])
                if dis < minDistance:
                    minDistance = dis
                    point1 = points[i]
                    point2 = points[j]
        return minDistance, point1, point2
    
    #recursive
    else:
        mid = len(points) // 2
        leftMinDistance, leftPoint1, leftPoint2 = shortest_distance(points[:mid])
        rightMinDistance, rightPoint1, rightPoint2 = shortest_distance(points[mid:])
        if leftMinDistance < rightMinDistance:
            minDistance = leftMinDistance
            point1 = leftPoint1
            point2 = leftPoint2
        else:
            minDistance = rightMinDistance
            point1 = rightPoint1
            point2 = rightPoint2

        #find the points that are close to the mid point
        midX = points[mid][0]
        minPoints = []
        for point in points:
            if abs(point[0] - midX) < minDistance:
                minPoints.append(point)


        #brute force comparison
        for i in range(len(minPoints)):
            for j in range(i+1, len(minPoints)):
                dis = distance(minPoints[i], minPoints[j])
                if dis < minDistance:
                    minDistance = dis
                    point1 = minPoints[i]
                    point2 = minPoints[j]
        
        return minDistance, point1, point2


def main():
    global count
    global rand
    # Open the text file in read mode
    with open('src/others/splashScreen.txt', 'r') as file:
        contents = file.read()
        print(contents)

    #input validations
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

    #generate random points
    points = []
    for i in range(n):
        point = []
        for j in range(d):
            point.append(random.uniform(0, rand))
        points.append(point)

    start = time.time()

    #sort the points based on x coordinate
    points = sort(points)

    #calculate the shortest distance
    minDistance, point1, point2 = shortest_distance(points)
    end = time.time()
    print('--------------------------------------------------------------------------------------------')
    print('Dua titik yang paling berdekatan:')
    print('Titik 1:',', '.join("{:.2f}".format(p) for p in point1))
    print('Titik 2:',', '.join("{:.2f}".format(p) for p in point2))
    print('\nJaraknya adalah: {:.2f}'.format(minDistance))
    print('Banyaknya operasi perhitungan rumus Euclidian: ', count)
    print('--------------------------------------------------------------------------------------------')
    print('Waktu eksekusi: {:.2f} ms'.format((end - start) * 1000))
    print(platform.processor())

    #plot the points
    plot.plot(points, point1, point2, rand)
   

if __name__ == '__main__':
    count = 0
    rand = 1000.0
    main()