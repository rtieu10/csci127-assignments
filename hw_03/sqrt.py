#Rachel Tieu & Emily Fang 
def mysqrt(n):
    i = 1
    oldguess = 1
    while i<=n:
        new = (oldguess+(n/oldguess))/2
        print(oldguess, new)
        if oldguess == new:
            break
        oldguess = new
print(mysqrt(3))
print(mysqrt(100))
    
    
