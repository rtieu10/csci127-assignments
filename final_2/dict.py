
def addline(d,line):
    line = line.lower()
    for word in line.split():
        if word[0] in d.keys():
            d[word[0]] = [word]
        else:
            d[word[0]] = [word]
    return d

d= {
    "h": "hello",
    "b":"bye",
    "a":"apple",
    "g":"goodbye",
    "s":"sleep",
    "f":"food",
    }

print(d)

addline(d,"How Are You Today?")
addline(d,"I Am Tired")
addline(d,"Who Is There")
addline(d,"When does the test start")
addline(d,"THANK YOU")

print(d) 

    #print(addline(d,line))

def spellcheck(d,word):
    word = word.lower()
    if word in d.values():
        return True
    else:
        return False
    
print(spellcheck(d,"pear"))
print(spellcheck(d,'g'))
print(spellcheck(d,"food"))