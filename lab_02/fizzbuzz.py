#Rachel Tieu & Lauren Piatt
def fizzbuzz(max_value):
    i=0
    while i <= 99:
        i = i + 1
        if i % 3 == 0:
            print ("Fizz")
        elif i % 5 == 0: 
            print ("Buzz")
        elif i % 5 == 0 and i % 3 == 0: 
            print ("FizzBuzz")
       
        else:
            print (i)
    
fizzbuzz(100)