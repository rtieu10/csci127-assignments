def compress_word(w):
    z = list(w)
    vowels = "AEIOUaeiou"
    s = [z[0]]
    for item in z:
        if item not in vowels:
            s.append(item)
            #s = w[0] + w.append(item)       
    w = "".join(s)
    print(z)
    return w

print(compress_word("apple"))


line = "Who is there"
def sentence(line):
    #z = line.split()
    vowels = "AEIOUaeiou"
    s = []
    for item in line.split():
        if item not in vowels:
            s.append(compress_word(item))
    #l = line.split() 
    return " ".join(s)
    
    
print(sentence(line))