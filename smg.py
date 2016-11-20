colour=["r","b","v","p","y","w","o","i"]
print("***************WELCOME TO THE MASTER MIND GAME******************")
import random
print("available colours=",colour)
temp=""
attempts=1
i=0
w=0
j=0
j=int(input("enter the number of elements to be guessed (no should be less than 8)"))
randcolour=random.sample(colour,j)
print("randomly choosen colours=",randcolour)
game="true"
for w in range (0,j):
  temp+="1"
while(game):
    if(attempts==(j+1)):
        print("\n you have already attempted",j,"times and you cannot play the game further")
        break
    loop=""
    ucolour=input("enter the colour sequence")
    ucolour=list(ucolour)
    if(attempts<=j):
        for i in range(0,j):
            if(ucolour[i]==randcolour[i]):
               loop+="1"
            else:
               loop+="0"
               
        print(loop)
        print("the characters 1 represents that the guess at\
              that position is correct and 0 repersents the wrong guess at that position")
        if((loop==temp)and (attempts==1)):
            print("\n","wow! you got the guess right in the first attempt")
            break
        if(loop==temp and attempts==2):
            print("\n"," you got the guess right in the 2nd attempt")
            break

        if(loop==temp and attempts==3):
            print("\n you got the guess right in the 3rd attempt")
            break
        if(loop==temp and attempts==4):
            print("\n you got the guess right in the 4th attempt")
            break
        if(loop==temp and attempts==5):
            print("\n you got the guess right in the 5th attempt")
            break
        if(loop==temp and attempts==6):
            print("\n you got the guess right in the 6th attempt")
            break
        if(loop==temp and attempts==7):
            print("\n you got the guess right in the 7th attempt")
            break

        attempts+=1
print("thankyou for playing srinkeths master mind game")
z=0
z=input("enter some value to exit")
