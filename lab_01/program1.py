def greetner(name):
    return "Hello "+name+"!"

print greeter ("Stan")

def make_abba(a, b):
  return a+b+b+a

def hello_name(name):
  return "Hello "+name+"!"

def sleep_in(weekday, vacation):
  if not weekday or vacation:   
    return True
  else: 
    return False

def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile :
    return True
  if not a_smile and not b_smile:
    return True
  return False