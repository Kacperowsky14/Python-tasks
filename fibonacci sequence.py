import time

x = 1 
y = 1
w = 2 
t = 3

z=int(input("Enter 1 to start the Fibonacci sequence. Enter zero to exit \n"))
while z != 0 and z != 1:
    print("Wrong command!")
    z=int(input("Let's try again \n"))
while z == 1:
    if t == 3:
        print("The first two numbers of the Fibonacci sequence are '1' and '1', the number three is '2'(sum of the two previous numbers)")
        time.sleep(4)
        w = x+y
        t += 1
    else: 
        x = y+w
        print("the ", t, " number is",x,) #4,7,10,13...n
        t += 1
        y = w+x
        print("the ", t, " number is",y,) #5,8,11,14...n
        t += 1
        w = y+x
        print("the ", t, " number is",w,) #6,9,12,15...n
        t += 1
        z = int(input("Keep counting? Yes-1 No-0 \n"))
        while z != 0 and z != 1:
            print("Wrong command!")
            z=int(input("Let's try again \n"))
if z == 0:
    print("Bye!")
    time.sleep(1)