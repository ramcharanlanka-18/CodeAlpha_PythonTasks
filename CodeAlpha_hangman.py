import random
def Hangman():
    lives=6
    words=["elephant","brush","strawberry","shirt","australia"]
    clues=["IT IS AN ANIMAL","IT IS A DRAWING INSTRUMENT","IT IS A FRUIT","CLOTHES WE WEAR","IT IS A COUNTRY"]
    now=random.randint(0,4)
    print("LETS PLAY HANGMAN GAME")
    print("YOU HAVE 5 CHANCES ONLY.YOU WILL BE LOSE FOR SIXTH INCORRECT GUESS")
    currentword=words[now]
    length=len(currentword)
    print("CLUE :"+clues[now])
    for i in range(length):
        print("_",end=" ")
    c=0
    status=["_"]*(length)
    while(True):
        while(True):
            print()
            print()
            u=input("GUESS THE LETTER :")
            user=u.lower()
            if len(user)>1 or user in status:
                print("please enter one letter which you do not entered before")
            else:
                break
        if(user in currentword):
            for i in range(length):
                if(currentword[i]== user):
                    status[i]=user
                    c=c+1
            print(status)    
            if c==length:
                print(" YOU WON THE GAME ")
                print(" CONGRATULATIONS ")
                break
            print()
        else:
            lives=lives-1
            if lives==5:
                print("YOU LOST ONE CHANCE.NOW YOU HAVE ONLY FIVE CHANCES")
                print("  +----+  ")
                print("  |    |  ")
                print("  |    0  ")
                print("  |       ")
                print("  |       ")
                print("  |       ")
                print(" -^-      ")
            elif lives==4:
                print("YOU LOST ANOTHER CHANCE.NOW YOU HAVE ONLY FOUR CHANCES")
                print("  +----+  ")
                print("  |    |  ")
                print("  |    0  ")
                print("  |    |  ")
                print("  |       ")
                print("  |       ")
                print(" -^-      ")
            elif lives==3:
                print("YOU LOST ANOTHER CHANCE.NOW YOU HAVE ONLY THREE CHANCES")
                print("  +----+  ")
                print("  |    |  ")
                print("  |    0  ")
                print("  |   /|  ")
                print("  |       ")
                print("  |       ")
                print(" -^-      ")
            elif lives==2:
                print("YOU LOST ANOTHER CHANCE.NOW YOU HAVE ONLY TWO CHANCES")
                print("  +----+  ")
                print("  |    |  ")
                print("  |    0  ")
                print("  |   /|\ ")
                print("  |       ")
                print("  |       ")
                print(" -^-      ")
            elif lives==1:
                print("YOU LOST ANOTHER CHANCE.NOW YOU HAVE ONLY ONE CHANCE")
                print("  +----+  ")
                print("  |    |  ")
                print("  |    0  ")
                print("  |   /|\ ")
                print("  |   /   ")
                print("  |       ")
                print(" -^-      ")
            elif lives==0:
                print("YOU LOST THE GAME , BETTER LUCK NEXT TIME ")
                print("  +----+  ")
                print("  |    |  ")
                print("  |    0  ")
                print("  |   /|\ ")
                print("  |   / \ ")
                print("  |       ")
                print(" -^-      ")
                break
Hangman()
while (True):
    again=input("WANNA PLAY THE GAME AGAIN?(YES / No) :").lower()
    if(again =="yes"):
        Hangman()
    else:
        print(" G A M E  O V E R  ")
        break

