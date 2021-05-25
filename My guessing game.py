#THIS IS A GUESSING GAME

#THIS IS WITHOUT EXCEPTION HANDLING

import random

#THIS A NORMAL FORM OF RANDOM LIBRARY

def easy():
    COUNT=0
    name1=str(input("PLEASE ENTER YOUR NAME="))
    name=name1.upper()
    # THIS IS A PASSWORD STATEMENT
    print("")
    password11=str(input("ENTER THE PASSWORD [IF KNOW] ="))
    password1=password11.upper()
    password="UJJU2003"
    for i in range (100):
        a=random.randint(1,10)
        COUNT=COUNT+1
        print("")
        print("                                                    THIS A NORMAL FORM OF RANDOM LIBRARY")
        print("")
        # IF USER ENTERED THE RIGHT PASSWORD
        if password == password1:
                print("YOU ENTERED THE RIGHT PASSWORD")
                print("")
                print("THE CORRECT ANSWER IS = ",a)
                print("")
                b=int(input("GUESS THE NUMBER [B/W - 0 TO 10] = "))
                if a==b:
                    print("")
                    print(name,"YOU WIN!!!")
                    break
                else:
                    print("")
                    print(name,"YOU LOSE!!!")
                    print("")
                    print("THE CORRECT ANSWER IS = ",a)
        # IF USER ENTERED THE WRONG PASSWORD
        else:
                print("")
                print("YOU ENTERED THE WRONG PASSWORD")
                print("MEANS YOU ARE THE USER !!!")
                print("")
                b=int(input("GUESS THE NUMBER [B/W - 0 TO 10] = "))
                if a==b:
                        print("")
                        print(name,"YOU WIN!!!")
                        break
                else:
                    print("")
                    print(name,"YOU LOSE!!!")
                    print("")
                    print("THE CORRECT ANSWER IS = ",a)
                    print("Better luck next time")
                    print("")
        print("")
        print("                           ==========================RESTART==========================")
    print("")
    print("TOTAL NUMBER OF PROGRAM EXECUTE = ",COUNT)
    print("")

#THIS IS A DECIMAL FORM OF RANDOM LIBRARY

def medium():
    COUNT=0
    name1=str(input("PLEASE ENTER YOUR NAME="))
    name=name1.upper()
    # THIS IS A PASSWORD STATEMENT
    print("")
    password11=str(input("ENTER THE PASSWORD [IF KNOW] ="))
    password1=password11.upper()
    password="UJJU2003"
    for i in range (100):
        a=random.random()
        A=round(a,2)
        COUNT=COUNT+1
        print("")
        print("                                                  THIS IS A DECIMAL FORM OF RANDOM LIBRARY")
        print("")
        print("                   THIS MODULE CONTAIN DECIMAL NUMBER PLEASE ENTER FLOATING NUMBER UPTO 2 PLACE")
        print("")
        # IF USER ENTERED THE RIGHT PASSWORD
        if password == password1:
                print("YOU ENTERED THE RIGHT PASSWORD")
                print("")
                print("YOU ENTERED CORRECT PASSKEY SO ANSWER IS = ",A)
                print("")
                b=float(input("GUESS THE NUMBER [B/W - 0 TO 1] DECIMAL INCLUDED = "))
                if A==b:
                    print("")
                    print(name,"YOU WIN!!!")
                    break
                else:
                    print("")
                    print(name,"YOU LOSE!!!")
                    print("")
                    print("THE CORRECT ANSWER IS = ",A)
        # IF USER ENTERED THE WRONG PASSWORD
        else:
                print("")
                print("YOU ENTERED THE WRONG PASSWORD")
                print("MEANS YOU ARE THE USER !!!")
                print("")
                b=float(input("GUESS THE NUMBER [B/W - 0 TO 1] DECIMAL INCLUDED = "))
                if A==b:
                        print("")
                        print(name,"YOU WIN!!!")
                        break
                else:
                    print("")
                    print(name,"YOU LOSE!!!")
                    print("")
                    print("THE CORRECT ANSWER IS = ",A)
                    print("Better luck next time")
                    print("")
        print("")
        print("                        ==========================RESTART==========================")
    print("")
    print("TOTAL NUMBER OF PROGRAM EXECUTE = ",COUNT)
    print("")

#THIS A UNIFORM FORM OF RANDOM LIBRARY

def hard():
    COUNT=0
    name1=str(input("PLEASE ENTER YOUR NAME="))
    name=name1.upper()
    # THIS IS A PASSWORD STATEMENT
    print("")
    password11=str(input("ENTER THE PASSWORD [IF KNOW] ="))
    password1=password11.upper()
    password="UJJU2003"
    for i in range (100):
        a=random.uniform(0,12)
        A=round(a,2)
        COUNT=COUNT+1
        print("")
        print("                                                  THIS IS A UNIFORM FORM OF RANDOM LIBRARY")
        print("")
        print("                   THIS MODULE CONTAIN DECIMAL NUMBER PLEASE ENTER FLOATING NUMBER UPTO 2 PLACE")
        print("")
        # IF USER ENTERED THE RIGHT PASSWORD
        if password == password1:
                print("YOU ENTERED THE RIGHT PASSWORD")
                print("")
                print("YOU ENTERED CORRECT PASSKEY SO ANSWER IS = ",A)
                print("")
                b=float(input("GUESS THE NUMBER [B/W - 0 TO 12] DECIMAL INCLUDED = "))
                if A==b:
                    print("")
                    print(name,"YOU WIN!!!")
                    break
                else:
                    print("")
                    print(name,"YOU LOSE!!!")
                    print("")
                    print("THE CORRECT ANSWER IS = ",A)
        # IF USER ENTERED THE WRONG PASSWORD
        else:
                print("")
                print("YOU ENTERED THE WRONG PASSWORD")
                print("MEANS YOU ARE THE USER !!!")
                print("")
                b=float(input("GUESS THE NUMBER [B/W - 0 TO 12] DECIMAL INCLUDED = "))
                if A==b:
                        print("")
                        print(name,"YOU WIN!!!")
                        break
                else:
                    print("")
                    print(name,"YOU LOSE!!!")
                    print("")
                    print("THE CORRECT ANSWER IS = ",A)
                    print("Better luck next time")
                    print("")
        print("")
        print("                        ==========================RESTART==========================")
    print("")
    print("TOTAL NUMBER OF PROGRAM EXECUTE = ",COUNT)
    print("")
	
#THE MAIN PROGRAMN STARTED FROM HERE

def main():
    print("")
    print("                                =========================GUESSING GAME=========================")
    print("")
    level=str(input("""CHOOSE YOUR LEVEL:
    1) EASY
    2) MEDIUM
    3) HARD
    PLEASE ENTER YOUR CHOICE {IN NUMBERS} = """))
    print("")
    if level=="1":
        easy()
    elif level=="2":
        medium()
    elif level=="3":
        hard()
    else:
        print("YOU ENTERED WRONG INFORMATION")
		
main()

#THIS IS A LOOPING STATEMENT

for i in range(100):
    print("")
    print("")
    print("                       =========================PROGRAM START AGAIN=========================")
    print("")
    print("")
    choice1=str(input("ARE YOU RE RUN THE PROGRAM {Y/N} = "))
    choice=choice1.upper()
    if choice=="Y" and "YES":
        main()
    elif choice=="N" and "NO":
        exit()
    else:
        print("PLEASE RE-ENTER THE INFORMATION")
