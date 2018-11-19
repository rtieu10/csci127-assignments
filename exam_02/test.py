def encode(s):
    l=[]
    count=1
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            count+=1
        else:
            x=[s[i],count]
            l.append(x)
            count=1
    l.append([s[-1],count])
    return l

print(encode('aaabbbccaaaddeee'))
x = encode('aaabbbccaaaddeee')


def decode(l):
    s = ""
    for i in l:
        for count in range(i[1]):
            s+=i[0]
    return s
        
            
print(decode(x))