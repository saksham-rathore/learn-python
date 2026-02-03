numbers = (1, 4, 9, 16, 25, 36, 49, 36, 64,  81, 100)

x = 36

i = 0 
while i < len(numbers):
    if(numbers[i] == x):
        print("found at index", i)
    i += 1


#break
i = 1
while i <= 5:
    print(i)
    if(i == 3):
        break
    i += 1 

print("end of loop")



i = 0 
while i <= 5:
    if(i == 3):
        i += 1 
        continue
    print(i)
    i += 1
    
