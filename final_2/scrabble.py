
def canMakeWord(letters,word):
    for chars in letters:
        lettercount = letters.count(chars)
    for letter in word:
        wordcount = word.count(letter)
    if wordcount > lettercount:
        return False
    else:
        return True
    
print(canMakeWord("ladilmy","daily"))
print(canMakeWord("eerriin","eerie"))
print(canMakeWord("orrpgma","program"))
print(canMakeWord("orppgma","program"))
print(canMakeWord("hhello","hello")) 
       
       
def canMakeWord(letters,word):
    for chars in letters:
        lettercount = letters.count(chars)
        wordcount = word.count(chars)
        if lettercount >= wordcount:
            return True
        else:
            return False 

print(canMakeWord("ladilmy","daily"))
print(canMakeWord("eerriin","eerie"))
print(canMakeWord("orrpgma","program"))
print(canMakeWord("orppgma","program"))
print(canMakeWord("hhello","hello")) 
    
            
            
            
            
# below this is the first code i tried, it does NOT work            
            
            
def canMakeWord(letters,word):#not working because technically the letters are still in there there just arent enough
    count=0
    lettercount=0
   # for chars in word:               #think of a way to actually count the letters in letters and compare it to the amount of letters in word
    #    if word[chars] == word[chars:]:
     #       count = count + 1
    #for chars in letters:
     #   if chars in word:
    for chars in letters:
        if letters[0] == letters[0:]:
            lettercount = lettercount + 1 
        #if chars not in letters:    # find a way to program it where it actually counts the letters and takes into mind if there are enough letters
         #   return False
        #else:
         #   return True
    for chars in word:
        if word[0] == word[0:]:
            count = count + 1
        if count < lettercount:
            return True
        else:
            return False
            
#print(canMakeWord("ladilmy","daily"))
#print(canMakeWord("eerrinn","eerie"))
#print(canMakeWord("orppgma","program"))
#print(canMakeWord("hello","by"))
            
            
            
            
            
            
            
            