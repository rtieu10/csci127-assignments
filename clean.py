def read(file):
    f = open(file)
    t = f.read()
    return t


#def clean_data(t):
 #   words = t.split() 
  #  for item in t:
   #     if t in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
    #        result = result + item.lower()
     #   else:
      #      result = result + " "
    #return result
        #if t in "!,.?:;-":
            #words.strip("!,.?:;-")

#def clean_punct(t):
 #   #words = t.split()
  #  words = t.split()
   # clean =[]
    #for item in t:
     #   if t in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
      #      s = item.lower()
       #     clean.append(s) 
       # if item in "!,.?:;-":
        #    str(words).strip("!,.?:;-")
         #   clean.append(words)
    #return clean
        
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

        
   