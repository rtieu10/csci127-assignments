filename = "moby-small.txt"

def build_word_counts(words):
    d={}
    for word in words.split():
        d.setdefault(word,0)
        d[word]=d[word]+1
    return d
        
def clean_data(s):
    result=""
    for letter in s:
        if letter in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            result = result + letter.lower()
        else:
            result = result + " "
    return result
#s = f.read()

#cleaned_string = clean_data(s) 
#words = build_word_counts(cleaned_string)
#val = words.values()      #you take the values from the dictionary called words
#vals = sorted(vals)
#print(vals) 
f = open(filename)
s = f.read()
words_uncleaned = build_word_counts(s)
print(words_uncleaned)
cleaned_string = clean_data(s)
print(cleaned_string)
print("-------------------")
words = build_word_counts(cleaned_string)
print(words)
common_words=[]
vals = words.values()
vals = sorted(vals)

for k in words:
    if words[k] > 1000:
        print(k,words[k])
        
#def build_phrases(cleaned_string):    #make a dictionary for every word that appears, mak an empty list as the value of the key and add the word after it to the list that makes up the value of the key 
 #   dict ={}
  #  for i in cleaned_string.split():
   #     #dict.setdefault(i,[])
    #    dict.setdefault(i,[]).append(dict[i+1])
    #return dict

#print(build_phrases(cleaned_string))

def build_phrases(cleaned_string):
    clean_list=cleaned_string.split()
    dict ={}
    for i in range(0,len(clean_list)-1):
        dict.setdefault(clean_list[i],[]).append(clean_list[i+1])
    return dict
             
print(build_phrases(cleaned_string))
 

