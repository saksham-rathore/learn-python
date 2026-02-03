'''
1 for snake 
-1 for water 
0 for gun
'''

computer = -1 
you = input("enter your choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "snake", -1: "water", 0: "gun"}

younum    = youDict[you]

print(f"you chose {reverseDict[you]}\ncomputer chose {reverseDict[computer]}")

if(computer == you):
    print("its a draw")

else:
    if(computer ==-1 and you ==1):
     print("you win")
     
     if(computer ==-1 and you ==0):
     print("you lose")

     if(computer ==1 and you ==0):
     print("you win")

     if(computer ==1 and you ==-1):
     print("you win")

     if(computer ==0 and you ==1):
     print("you win")

     if(computer ==0 and you ==-1):
     print("you lose")




