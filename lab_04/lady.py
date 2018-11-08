def happyLadybugs(b):
    for character in b:                                     #for each character in the string b 
        if character != "_" and b.count(character) == 1:
            return "NO"
        
        
        if b.count("_") == 0:
            for i in range(1,len(b)-1):                     #make it len(b)-1 because the last string wont have a character after it you can start at 1 and check the one before it or 0 and check the one after 
                if b[i-1] != b[i] and b[i+1] != b[i]:
                    return "NO"
        
    return "YES"

print(happyLadybugs("ABCC_ACB"))
print(happyLadybugs("AAB"))
print(happyLadybugs("AABB"))

#if theres a space you need at least 2 ladybugs of the same color
#there needs to be at least 2 ladybugs of each color and at least one space
#if there is a space then you only need to determine if theres at least 2 of every color
#you can use what we need in the mode function to see how many o the letter there are
#you can use the sorted command where you can sort it in a list and check the amount

