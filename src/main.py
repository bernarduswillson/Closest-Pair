import math
import time
import random
import platform

#import from files
import algorithm.divideAndConquer as divideAndConquer
import algorithm.bruteForce as bruteForce
import others.plot as plot


# euclidian distance counter
count = 0
# random number range
rand = 1000.0

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
points = divideAndConquer.quickSort(points)

# calculate the shortest distance
minDistance, point1, point2, count = divideAndConquer.DnCShortestDistance(points, rand, count)
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
minDistance, point1, point2, count = bruteForce.BFShortestDistance(points, rand, count)
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
print('--------------------------------------------------------------------------------------------')
print('Device:', platform.processor())