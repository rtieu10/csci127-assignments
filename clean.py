def read(file):
    f = open(file)
    t = f.read()
    return t

def clear(t):
    word =""
    x = t.lower()
    for i in x:
        if i in 'abcdefghijklmnopqrstuvwxyz':
            word += i
        else:
            word+= " "
    return word 
        
def word_count(t):
    count = 0 
    for item in t:
        if item in 'abcdefghijklmnopqrstuvwxyz':
            count = count + 1
    return count

print(clear("macbeth.txt")) 
print(word_count("macbeth.txt"))
print("--------------") 
print(clear(",..,,.,helloooooo"))
print(word_count(",..,,.,helloooo"))

        
   
