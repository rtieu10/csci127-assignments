l = [1,2,3,4,5,6,7,8,9,10]

def filterodd(l):
    l2 = []
    num = 0 
    for num in l: 
         if num % 2 == 1:
            l2.append(num)
    return l2

print(filterodd(l))



def mapsquare(l):
    l2=[]
    num = 0
    for num in l:
        num = num*num
        l2.append(num)
    return l2

print(mapsquare(l)) 