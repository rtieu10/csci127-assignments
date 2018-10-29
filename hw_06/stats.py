#Madison Chen & Rachel Tieu


import random
l = [] 
for i in range(0,100):
    l. append(random.randrange(0,11))

print(l) 

def max(a):
    a = 0
    large = a[x]
    while x < len(a):
        if a[x] > large[x]:
            large = a[x]
        x = x + 1
    return large

print(max(l))


def index_largest(l):
    l1 = 0
    for i in range(1,len(1)):
        if l(i) > l[li]:
            li = i
        return li
    

def frequency(list, a):
    count = 0
    for x < len(l):
        if num in l:
            count = count + 1
        return count

  def mode(l):   
    mmode=0
    u=[]
    num=0
    for i in l:
        if i not in u:
            mode=frequency(l,i)
            if mode>mmode:
                mmode=mode
                num=i
            u.append(i)
    return num,mmode

print(mode(l)) 
      
    
