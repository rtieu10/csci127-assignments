def makeacronym(w):
    s = w.split()
    for words in s:           #splits all the words in w into a string of individual words
      acronym = words[0]
      print (acronym)
      
print(makeacronym("Laugh Out Loud"))
print(makeacronym("In my humble opinion"))
    
    
    
    
    
    #if i in len(w+1):
        #acronym = w[i] 
        #first = i[0]
            #irst = w[i]
            #second = w[i+1]
            
            
    #print(words[0])
       #i = words[0] 
       #first = words[0]
       #second = words[1]
       #acronym = first + second 
            
    #return acronym