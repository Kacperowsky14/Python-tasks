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
        if t == 31 or t == 61 or t == 91 or t == 121 or t == 151 or t == 181 or t == 211:
            z = int(input("Keep counting? Yes-1 No-0 \n"))
            while z != 0 and z != 1:
                print("Wrong command!")
                z=int(input("Let's try again \n"))
        if t == 241:
            print("My memory can't take anymore ...")
            time.sleep(1)
            z = "dafuuuuuq"
if z == 0:
    print("Bye!")
    time.sleep(1)
if z == "dafuuuuuq":
    print("I'm leaving, forgive me ...")
    time.sleep(3)

# there is more fun in this code, the full version is vol.1