def score(x):
    one = "AEIOULNRSTaeioulnrst"
    two = "DGdg"
    three = "BCMPbcmp"
    four = "FHVWYfhvwy"
    five = "Kk"
    eight = "JXjx"
    ten = "QZqz"
    thescore = 0
    for i in x: 
        if i in one:
            thescore += 1
        elif i in two:
            thescore += 2
        elif i in three:
            thescore += 3
        elif i in four:
            thescore += 4
        elif i in five:
            thescore += 5
        elif i in eight:
            thescore += 8
        elif i in ten:
            thescore += 10
    return thescore

print(score("HELLO"))