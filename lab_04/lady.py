def happyLadybugs(b):
    for character in b:                                     #for each character in the string b 
        if character != "_" and b.count(character) == 1:
            return "NO"
        
        
        if b.count("_") == 0:
            for i in range(1,len(b)-1):                     #make it len(b)-1 because the last string wont have a character after it you can start at 1 and check the one before it or 0 and check the one after 
                if b[i-1] != b[i] and b[i+1] != b[i]:
                    return "NO"
        
    return "YES"

<<<<<<< HEAD
=======
#print(happyLadybugs("ABCC_ACB"))
#print(happyLadybugs("AAB"))
#print(happyLadybugs("AABB"))


>>>>>>> 2f66f65d610bdb1422329a8f069daacb54e9cebc
def happy(s):
    if '_' not in b:
        for i in range(1,len(b)-1):
            if b[i-1] != b[i] and b[i+1] != b[i]:
                return "NO"
    else:
        vals = dict(b).values()
        if l in vals:
            return "NO"
    return "YES"

def dict(x):
    d = {}
    for i in x:
        if i != "_":
            if i not in d: 
               d[i] = 1
        else:
            d[i] += 1
    return d 

a = 'AABCBD_'
b = 'ABB'
c = '____'
d = 'ABABAB'
e = 'A_BBA'


print(happy(a))
print(happy(b))
print(happy(c))
print(happy(d))
print(happy(e)) 

print(happyLadybugs("ABCC_ACB"))
print(happyLadybugs("AAB"))
print(happyLadybugs("AABB"))
print(happyLadybugs("A_C_BB"))
print(happyLadybugs("ABCBC_A"))



#if theres a space you need at least 2 ladybugs of the same color
#there needs to be at least 2 ladybugs of each color and at least one space
#if there is a space then you only need to determine if theres at least 2 of every color
#you can use what we need in the mode function to see how many o the letter there are
#you can use the sorted command where you can sort it in a list and check the amount


<<<<<<< HEAD
=======

>>>>>>> 2f66f65d610bdb1422329a8f069daacb54e9cebc
