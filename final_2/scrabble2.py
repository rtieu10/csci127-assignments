def canMakeWord(letters,word):
    for chars in letters:
        lettercount = letters.count(chars)
        wordcount = word.count(chars)
        if (lettercount < wordcount):
            return False 
    return True
print(canMakeWord("ladilmy","daily"))
print(canMakeWord("eerriin","eerie"))
print(canMakeWord("orrpgma","program"))
print(canMakeWord("orppgma","program"))