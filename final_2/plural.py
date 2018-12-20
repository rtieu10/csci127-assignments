def countPlurals(line):
    count = 0
    for letters in line.split():
        if letters[-1] == "s":
            count = count + 1
    return count
print(countPlurals("gorillas cats dogs"))
print(countPlurals("dog gorilla"))
print(countPlurals("gorillas dog cat"))
print(countPlurals("sally sells shells by the seashore")) 
print("--------------------------")
def notPossesive(line):
    count = 0 
    for letters in line.split():
        if letters[-1] == "s" and letters[-2] != "'":
            count = count + 1
    return count
print(notPossesive("gorillas gorilla's cats"))
print(notPossesive("cat's"))
print(notPossesive("hello"))
print(notPossesive("sally's sandwiches"))
print(notPossesive("rachel's exams"))