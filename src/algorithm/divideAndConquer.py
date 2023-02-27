import math


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
    

# calculate the distance between two points and count the number of distance calculation
def euclidianDistance(p1, p2, count):
    count += 1
    dis = 0
    for i in range(len(p1)):
        dis += (p1[i] - p2[i]) ** 2
    return math.sqrt(dis), count


# find the shortest distance between two points
def DnCShortestDistance(points, rand, count):
    # even number of points base
    if len(points) == 2:
        minDistance, count = euclidianDistance(points[0], points[1], count)
        return minDistance, points[0], points[1], count
    
    # odd number of points base, brute force
    elif len(points) == 3:
        minDistance = rand*rand
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
    
    # recursive finding the shortest distance
    else:
        mid = len(points) // 2
        leftMinDistance, leftPoint1, leftPoint2, count = DnCShortestDistance(points[:mid], rand, count)
        rightMinDistance, rightPoint1, rightPoint2, count = DnCShortestDistance(points[mid:], rand, count)
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
                    dis, count = euclidianDistance(midPoints[i], midPoints[j], count)
                    if dis < minDistance:
                        minDistance = dis
                        point1 = midPoints[i]
                        point2 = midPoints[j]
        
        return minDistance, point1, point2, count