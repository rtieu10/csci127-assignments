
    
def vowel_pig_latin(name):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    name_start= name[0]
    if name_start in vowels:
        return(name + "ay")
    else:
        return name[1:] + name[0] + "ay"

print(vowel_pig_latin("apple"))
print(vowel_pig_latin("Orange"))
print(vowel_pig_latin("Hello"))
print(vowel_pig_latin("bye"))

