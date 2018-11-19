def encode(x):
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
        
        
    
        
    
    
