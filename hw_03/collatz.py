def collatz(a):
    c = 0
    while a > 1:
        if a % 2 == 0:
            a = a / 2
            print(int(a))
            c = c + 1
        else:
            a = 3*a + 1
            print (a)
            c= c + 1
    return("The input has ran ", c, "times in this code")
print(collatz(7))
print(collatz(6))