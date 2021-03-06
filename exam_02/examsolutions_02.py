def make_acronym(word):
    result = ""
    for letter in word.split():
        result = result + word[0]
    return result

def rle1(line):
    enoceded = []
    i = 0
    while i < len(line)-1:          #the for loop goes over everything in the list in the while loop you can use the index giving you more control
        next_letter = i + 1
        while next_letter < len(line) and line[next_letter] == line[1]:  
            next_letter = next_letter + 1
            encoded.append([next_letter -1,line[i]])
            i = next_letter
    if i == len(line) -1:
        enoded.append([1,line[i]])
    return encoded

def rle2(line):
    encoded = []
    count = 1
    prevchar = line[0]
    for c in line[1:]:                  #setting one variable after another -> piggybacking
        if c == prevchar:               #if the current character is the same as the one before it then it will + 1
            count = count + 1
        else:
            encoded.append([count, prevchar]) 
            count = 1
            prevchar = c
    encoded.append([count,prevchar])
    return encoded

def decode(encoded):
    result = ""
    for item in encoded:
        result = result + item[0] + item[1]
    return result


def score1(word,scores):
    score = 0
    for letter in word: 
        for k in scores:
            if letter in k:
                score = score + scores[k]
    return score

def score2(word, scores_raw):
    scores = {}
    for k in scores_raw:
        for letter in k:
            scores[letter] = scores_raw[k]
    score = 0
    
            
