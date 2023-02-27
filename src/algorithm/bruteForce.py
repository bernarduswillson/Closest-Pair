import math


# calculate the distance between two points and count the number of distance calculation
def euclidianDistance(p1, p2, count):
    count += 1
    dis = 0
    for i in range(len(p1)):
        dis += (p1[i] - p2[i]) ** 2
    return math.sqrt(dis), count


#brute force comparison
def BFShortestDistance(points, rand, count):
    minDistance = rand * rand
    point1 = points[0]
    point2 = points[1]
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            dis, count = euclidianDistance(points[i], points[j], count)
            if dis < minDistance:
                minDistance = dis
                point1 = points[i]
                point2 = points[j]
    return minDistance, point1, point2, count