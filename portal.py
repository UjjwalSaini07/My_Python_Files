import random 
game= ["UJJWAL","VIKAS"]
pubg= ["ujjwal2003","1234567890"]
for I in range (1000):
    A=str(input("ENTER YOU RUN THE PROGRAM HERE{Y/N}="))
    Ae=A.upper()
    if Ae=="Y":
	print("          ======S. B.MILLS SER. SECONDARY SCHOOL=====")
	print("""THESE ARE SIX OPTION
	PRESS YOUR CHOICE
	1) CREATE A NEW ACCOUNT
	2) REMOVE THE ACCOUNT
	3) CHECK WHETHER YOUR ACCOUNT REGISTERED OR NOT
	4) EDIT YOUR ACCOUNT 
	5) ABOUT THE PROGRAM 
	6)FORGOT A PASSWORD """)
	choice=str(input("ENTER YOUR OPTION="))

# CREATE A NEW ACCOUNT

	if choice=="1":
	    print("ARE YOU SURE YOU CREATE YOUR NEW ACCOUNT")
	    a=str(input("ENTER YOUR FIRST NAME="))
	    be=a.upper()
	    if be in game:
		print("YOUR NAME IS ALREADY ADDED IN SERVER LIST")
	    else:
		b=str(input("ENTER THE LAST NAME="))
		c=str(input("ENTER THE PASSWORD="))
		d=str(input("CONFIRM YOUR PASSWORD="))
		if c==d:
		    print("YOUR PASSWORD MATCHED SUCCESSFULLY")
		    d=str(input("ENTER YOUR VALID EMAIL-ID="))
		    de=str(input("ENTER YOUR MOBILE NO.="))
		    e=random.randint(1000,9999)
		    print("THIS IS THE OTP=",e)
		    f=str(input("ENTER THE OTP HERE THE CREATE ACCOUNT="))
		    print("YOUR ACCOUNT REGISTERED SUCCESSFULLY")
		    game.append(a)
		    print(game)
		else:
		    print("SORRY YOUR PASSWORD NOT MATCH PLEASE RE-RUN THE PROGRAM")

#REMOVE THE ACCOUNT
		    
	if choice=="2":
	    print("ARE YOU SURE YOU REMOVE YOUR ACCOUNT")
	    g=str(input("ENTER THE USERNAME="))
	    ge=g.upper()
	    h=str(input("ENTER YOUR PREVIOUS PASSWORD="))
	    print(game)
	    game.remove(g)
	    print(game)

#CHECK WHETHER YOUR ACCOUNT REGISTERED OR NOT
	    
	if choice=="3":
	    print("ARE YOU SURE YOU CHECK YOURACCOUNT IS REGISTRED OR NOT")
	    i=str(input("ENTER THE USERNAME="))
	    ie=i.upper()
	    j=str(input("ENTER THE PASSWORD="))
	    if ie in game:
		print("YOUR ACCOUNT REGISTRED IN OUR SERVER LIST")
		print("WITH USER NAME=",i)
		print("WITH PASSWORD=",j)
	    else:
		print("""SORRY YOUR ACCOUNT NOT REGISTERED YET 
IF YOU REGISTER THE ACCOUNT SO PRESS 1
WHILE RESTRAT THE PROGRAM """)

#EDIT YOUR ACCOUNT
		
	if choice=="4":
	    print("ARE YOU SURE YOU EDIT YOUR ACCOUNT")
	    print("")
	    print("""ENTER THE NUMBER WHICH YOU EDITED 
	1) USERNAME 
	2) MOBILE  NUMBER
	3) EMAIL-ID """)
	    user=str(input("ENTER YOUR EDITED NUMBER="))
	    if user=="1":
		k=str(input("ENTER YOUR PREVIOUS USERNAME="))
		ke=k.append()
		game.remove(ke)
		l=str(input("ENTER THE NEW USERNAME="))
		le=l.upper()
		game.append(le)
		print("YOUR ACCOUNT IS UPDATED WITH YOUR EDITED INFORMATION ")
	    if user=="2":
		mp=str(input("ENTER YOUR PREVIOUS PASSWORD="))
		np=str(input("ENTER THE NEW PASSWORD="))
		print("YOUR ACCOUNT IS UPDATED WITH YOUR EDITED INFORMATION ")
	    if user=="3":
		o=str(input("ENTER THE PREVIOUS EMAIL-ID="))
		p=str(input("ENTER THE NEW EMAIL-ID="))
		print("YOUR ACCOUNT IS UPDATED WITH YOUR EDITED INFORMATION ")
	    else:
                print("INVALID")

# ABOUT THE PROGRAM

	if choice=="5":
	    print("""ABOUT PROGRAM
1) PROGRAMMER NAME = UJJWAL SAINI
2) TASK GIVEN BY = VIKAS SHARMA {SIR}
3) PRINCIPAL NAME = MRS.PREETI SHUKLA
4) SCHOOL = S.B.MILLS SER.SECONDARY SCHOOL
5) PROGRAMMING LANGUAGE USED = PYTHON IDE
6) MAIN CONCEPT OF PROGRAM IS = PORTAL
7) CLASS = 11th B""")

# FORGOT A PASSWORD

	if choice=="6":
	    q=str(input("ENTER THE USERNAME="))
	    r=str(input("ENTER THE PREVIOUS PASSWORD="))
	    re=random.randint(10000,99999)
	    print("       THE OTP IS =",re)
	    s=str(input("ENTER YOUR MOBILE NUMBER="))
	    t=str(input("ENTER NEW PASSWORD="))
	    pubg.append(t)
	    u=str(input("CONFIRM YOUR PASSWORD="))
	    if t==u:
		print("YOUR PASSWORD IS MATCHED SUCCESSFULLY ")
		print("YOUR PASSWORD IS UPDATED ")
		print("NOW REMEMBER THE PASSWORD ")
	    else:
		print("SORRY YOUR PASSWORD IS NOT MATCHED")

		print("RE-RUNTHE PROGRAM ")
	elif Ae=="N":
		print("GOODBYE")
		exit()
print("GOODBYE ●_●")
print("")
