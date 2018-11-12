import random
dict = {}
dict['NOUNS'] = ['dog','sandwich','cat','food','frog']
dict['VERBS'] = ['ate','walked','ran','skipped']
dict['HEROS'] = ['Spiderman','Hulk','Flash']
dict['ADJECTIVES'] = ['fast','slow','tired']
#NOUNS = ['dog','sandwich','cat','food','frog']
#VERBS = ['ate','walked','ran','skipped']
#HEROS = ['Spiderman','Hulk','Flash']
#ADJECTIVES = ['fast','slow','tired']

sentence = "<ADJECTIVES> <HERO> <VERB> in the <NOUNS> and then <HERO> <VERB> <NOUNS> later."

#if 'nouns' in dict:       #to check if the key exists 
 #   print("YES")


def madlib(s,d):
    new_list = []
    H_random = random.choice(d['HEROS'])
    for item in s.split():
        if item == "<NOUNS>":
            new_list.append(random.choice(dict['NOUNS']))
        elif item == "<VERB>":
            new_list.append(random.choice(dict['VERBS']))
        elif item == "<HERO>":
            new_list.append(H_random)
        elif item == "<ADJECTIVES>":
            if sentence.index("<ADJECTIVES>") == 0:
                #new_list.append(random.choice(ADJECTIVES))
                n = random.choice(dict['ADJECTIVES'])
                n = n.capitalize()
                new_list.append(n)
        else:
            new_list.append(item)
            
    return " ".join(new_list)

print(madlib(sentence,dict))
