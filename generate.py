import random

num = input("how many points would you like to generate? : ")
f = open('point.txt', 'w')
r = str(num) + "\n"
f.write(r)

for i in range(0,num):
    x = random.randint(0,100)
    y = random.randint(0,100)
    p = str(x) +" " + str(y) + "\n"
    f.write(p)

f.close
