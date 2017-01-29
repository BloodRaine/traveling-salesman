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
        return float(math.sqrt((self.x-p.x)**2+(self.y-p.y)**2))
    def __str__(self):    # All we have done is renamed the method
         return "({0}, {1})".format(self.x, self.y)
    def __repr__(self):
        return str(self)
    def compare(self, x):
        if self.x == x.x and self.y == x.y:
            return True
        else:
            return False

def cost(arr):
    ar = list(arr)
    p0 = ar[0]
    ar.remove(p0)
    s = 0
    p_end = p0
    n = p0
    c = 0
    while ar:
        c+=1
        m = n.distance(ar[0])
        for p in ar:
            if n.distance(p) <= m:
                m = n.distance(p)
                p_end = p
        s += m
        n = p_end
        ar.remove(p_end)
    s += p0.distance(p_end)
    return s

# main

text_file = open("test.txt", "r")
print "Opening test file"
first_line = int(text_file.readline().strip())

l = []
for line in text_file:
    x,y = line.split()
    p = Point(int(x),int(y))
    l.append(p)

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
    text += "brute force"
    l.remove(p0)
    for p in itertools.permutations(l):
        a = [p0] + list(p)
        m = float("inf")
        if cost(a) <= m:
            total = cost(a)
            path = a
    path.append(path[0])


print "The path generated from the %s algorithm is as follows" %text
print(path)
print "This is completed in a distance of %f units" %total
print "The time it took to calculate this was %f seconds" %(time.time() - start_time)
