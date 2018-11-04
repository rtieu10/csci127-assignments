def happyLadybugs(b):
    for character in b:
        if character != "_" and b.count(character) == 1:
            return "NO"
        
        
        if b.count("_") == 0:
            for i in range(1,len(b)-1):
                if b[i-1] != b[i] and b[i+1] != b[i]:
                    return "NO"
        
     return "YES"

print(happyLadybugs("ABCC_ACB"))
print(happyLadybugs("AAB"))
print(happyLadybugs("AABB"))