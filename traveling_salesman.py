#!/usr/bin/python
# Robinson Merillat
# CSCI 406
# Project 1 - Traveling Salesman

import math
import itertools
import time

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self,p):
        return math.sqrt((self.x-p.x)**2+(self.y-p.y)**2)
    def __str__(self):    # All we have done is renamed the method
         return "({0}, {1})".format(self.x, self.y)
    def __repr__(self):
        return str(self)

def cost(arr):
    n = len(arr)
    total_dist = 0 
    for i in range(0, n - 1):
        total_dist += arr[i].distance(arr[i + 1])
    return total_dist + arr[-1].distance(arr[0])

def cost_old(arr):
    ar = list(arr)
    p0 = ar[0]
    ar.remove(p0)
    s = 0
    p_end = p0
    n = p0
    infin = float("inf")
    while ar:
        for p in ar:
            m = infin
            temp = n.distance(p)
            if temp < m:
                m = temp
                p_end = p
        s += m
        n = p_end
        ar.remove(p_end)
    s += p0.distance(p_end)
    return s

# main

text_file = open("point.txt", "r")
print "Opening test file"
first_line = int(text_file.readline().strip())

l = []
for line in text_file:
    x,y = line.split()
    p = Point(int(x),int(y))
    l.append(p)

text_file.close

path = []
p0 = l[0]
total = 0
text = ""
method = raw_input("Would you like to perform the nearest neighbor or brute force algoritm? (enter NN or BF): ")
start_time = time.time() 
if method == 'NN':
    l.remove(p0)
    path.append(p0)
    p_end = p0
    n = p0
    text += "nearest neighbor"
    while l:
        m = n.distance(l[0])
        for p in l:
            if n.distance(p) <= m:
                m = n.distance(p)
                p_end = p
        total += m
        n = p_end
        l.remove(p_end)
        path.append(p_end)
    total += p0.distance(path[len(path)-1])
    path.append(p0)
elif method == 'BF':
    total = 100000000000
    text += "brute force"
    l.remove(p0)
    for p in itertools.permutations(l):
        a = (p0,) + p
        temp = cost(a)
        if temp < total:
            total = temp
            path = a
    path = path + (path[0],)

print "The path generated from the %s algorithm is as follows" %text
print(path)
print "This is completed in a distance of %f units" %total
print "The time it took to calculate this was %f seconds" %(time.time() - start_time)
