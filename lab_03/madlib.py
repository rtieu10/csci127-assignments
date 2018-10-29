#  Rachel Tieu and Emily Fang
import random
NOUNS = ['dog','sandwich','cat','food','frog']
VERBS = ['ate','walked','ran','skipped']
HEROS = ['Spiderman','Hulk','Flash']
ADJECTIVES = ['fast','slow','tired']

sentence = "<ADJECTIVES> <HERO> <VERB> in the <NOUNS> and then <HERO> <VERB> <NOUNS> later."

def madlib(s):
    new_list = []
    H_random = random.choice(HEROS)
    for item in s.split():
        if item == "<NOUNS>":
            new_list.append(random.choice(NOUNS))
        elif item == "<VERB>":
            new_list.append(random.choice(VERBS))
        elif item == "<HERO>":
            new_list.append(H_random)
        elif item == "<ADJECTIVES>":
            if sentence.index("<ADJECTIVES>") == 0:
                #new_list.append(random.choice(ADJECTIVES))
                n = random.choice(ADJECTIVES)
                n = n.capitalize()
                new_list.append(n)
        else:
            new_list.append(item)
            
    return " ".join(new_list)

print(madlib(sentence))
            
# NOUNS[random.randrange(0,len(NOUNS))] this also picks a random word within the length range
# sub = random.choice(NOUNS) , return sub
# def madlibify(sentence, nouns, verbs) - allows us to see the variables we are actually inputting here
# sentence.split() to convert it into a list of words
# you can make the result  a string to begin with which prevens you from using the join fucntion, you could
# have used a string or a list "result = result + " " + word
# we are appending words to a list which will eventually become a sentence, which is why we are randomly
# picking and we will eventually ask for the list / string to be returned which will appear as a sentence 
