<<<<<<< HEAD
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
=======
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
  if i in two: 
    thescore += 2 
  if i in three: 
    thescore +=3 
  if i in four: 
    thescore +=4 
  if i in five: 
    thescore += 5 
  if i in eight: 
    thescore += 8 
  if i in ten: 
    thescore += 10 
return thescore
  
print(thescore("AEIOU")) 
print(thescore("hello")) 
print(thescore("Hi")) 
>>>>>>> 9ba6f4d7af80b54d16d65a392e7b6141926c2ee8
