import math
import time
import random
import matplotlib.pyplot as plt
import others.plot as plot


#calculate the distance between two points and count the number of distance calculation
def distance(p1, p2):
    global count
    count += 1
    dis = 0
    for i in range(len(p1)):
        dis += (p1[i] - p2[i]) ** 2
    return math.sqrt(dis)

#find the shortest distance between two points
def shortest_distance(points):
    #sort the points based on x coordinate
    points = sorted(points, key=lambda point: point[0])

    #even number of points base
    if len(points) == 2:
        return distance(points[0], points[1]), points[0], points[1]
    
    #odd number of points base
    elif len(points) == 3:
        min_distance = rand
        point1 = points[0]
        point2 = points[1]
        #brute force comparison
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                dis = distance(points[i], points[j])
                if dis < min_distance:
                    min_distance = dis
                    point1 = points[i]
                    point2 = points[j]
        return min_distance, point1, point2
    
    #recursive
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

        #find the points that are close to the mid point
        mid_x = points[mid][0]
        mid_points = []
        for point in points:
            if abs(point[0] - mid_x) < min_distance:
                mid_points.append(point)

        #brute force comparison
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
    # Open the text file in read mode
    with open('src/others/splashScreen.txt', 'r') as file:
        contents = file.read()
        print(contents)

    n = int(input('Masukkan jumlah titik: '))
    d = int(input('Masukkan jumlah dimensi: '))

    #generate random points
    points = []
    for i in range(n):
        point = []
        for j in range(d):
            point.append(random.randint(0, rand))
        points.append(point)
    start = time.time()

    #calculate the shortest distance
    min_distance, point1, point2 = shortest_distance(points)
    end = time.time()
    print('--------------------------------------------------------------------------------------------')
    print('Dua titik yang paling berdekatan:\n', point1, "dan", point2)
    print('Jaraknya adalah: ', min_distance)
    print('Banyaknya operasi perhitungan rumus Euclidian: ', count)
    print('--------------------------------------------------------------------------------------------')
    print('Execution Time: ', end - start)

    plot.plot(points, point1, point2, rand)
   

if __name__ == '__main__':
    count = 0
    rand = 1000
    main()