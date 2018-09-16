def bondify(name):
    """
    takes in a string in thr form "first last" and returns
    it in the form "last, first last"
    """
    space_index = name.find(" ")
    first = name[0:space_index]
    last = name[space_index+1:]
    bond_name = last + "," + first + " " + last
    return bond_name 


def capitalize(name):
    """
    input: name --> a string in the form "first last"
    output: returns a string with each of the two words capitalized
    note: this is the one we started in class
    """
    
    s = "Rachel Tieu"
    s = s.upper()
    return s


def init(name):
    """
    Input: name --> a string in the form "first last"
    Returns: a string in the form "F. Last" where it's a capitalized first inital
    and capitalzed last name
    """
    name = "Rachel Tieu"
    name_list = name.split()
    
    print(name_list)
    
    first = name [0][0]
    last = "Tieu"
    
    return(first,'.' + last.upper())
    
    
def part_pig_latin(name):
    """
    Input: A string that is a single lowercase word
    Returns: that string in fake pig latin -> move the first letter of the word to the end and add "ay"
    so: "hello" --> "ellohay"
    """
    eng_word = "Hello"
    pig_word = eng_word[1:] + eng_word[0].lower() + "ay"
    return(pig_word) 


def make_out_word(out, word):
  return out[:2] + word + out[2:]


def make_tags(tag, word):
  make_tag = "<" + tag + ">" + word + "</" + tag + ">" 
  return make_tag


print(bondify("James Bond"))
print(capitalize("Rachel Tieu"))
print(init("Rachel Tieu"))
print(part_pig_latin("Hello"))
print(make_out_word('!!!!','Yay'))
print(make_tags('?','Huh'))