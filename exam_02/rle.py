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


"""def encode(x):
    dict = {}
    for letter in x:
        dict.setdefault(letter,0)
        dict[letter] = dict[letter] + 1
    return dict
print(encode("aabbccddd"))
print(encode("abcd"))


def encode(x):
    dict = {}
    for letter in x:
        dict.setdefault(letter,0)
        dict[letter] = dict[letter] + 1
        return [letter, dict[letter]] 
    for key,value in dict.items():
        dicttwo= []
        d = [key,value]
        dicttwo.append(d) 
        return dicttwo
print(encode("abcd"))
print(encode("aaabbbccdd"))
"""


#def encode(x):
 #   dict = {}
  #  for letter in x:
   #     dict.setdefault(letter,[])
        #dict[letter] = dict[letter].append
    #return dict

#print(encode("abcd"))
        
#def encode(x):
 #   dict = {}
  #  for letter in x:
##        dict.setdefault(letter,0)
       # dict[letter] = dict[letter] + 1
        
    #return dict
       
       
def decode(x):
    z = x.split() 
    for elements in z:              #split the list of lists? element is each list 
        letter = elements[0]        
        number = elements[1]
        total = letter * number     #you can try to use .join to join the whole string together again
