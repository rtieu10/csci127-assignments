def countApplesandOranges(s, t, a, b, apples, oranges):
    
    apple_location = []                    #list that will hold the numbers of the positions of the apples
    orange_location = []                   # list that will hold the numbers of the positions of oranges
    a_count = 0                            #count of the apples and oranges both start at 0 
    o_count = 0
    for i in apples:                       #for every element in the list apples
        apple_location.append(a + i)       #add each number in the list to a to get the position of the apple and append to the apple_location list 
    for i in apple_location:               #for every element in the apple_location list
        if i >= s and i <= t:              #check if the number is in the range s & t 
            a_count = a_count + 1          #if it is, add one to the count
    for i in oranges:                      #same for oranges
        orange_location.append(b + i)
    for i in orange_location:
        if i >= s and i <= t: 
            o_count = o_count + 1
    return a_count, o_count                #return the number of apples and oranges
apples = [1, -3, -5, 4]                    #list with numbers indicating how far it is from the apple tree (a) and (o) 
oranges= [3, -4, 6, -2]

print(countApplesandOranges(10, 15, 7, 18, apples, oranges)) #returns all the number of apples and oranges that are within the range of s&t