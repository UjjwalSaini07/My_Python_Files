import time
import random
import qrcode
import os

name = ["UJJWAL"]
date = ["1 jan 2020"]
age = ["17"]
passen = ["1", "10"]
local = ["DELHI"]


# FUNCTION OF RESERVATION OF TICKET
def reservationticket():
    print("")
    print("       ============RESERVATION OF TICKET=============")
    print("")
    ae1 = str(input("ENTER THE NUMBER OF PASSENGER="))
    try:
        ae = int(ae1)
        for in1 in range(ae):
            b = str(input("ENTER THE PASSENGER NAME="))
            be = b.upper()
            name.append(be)
            c = str(input("ENTER THE AGE="))
            age.append(c)
            cb = input("ENTER THE GENDER=")
            print("")
        print("ENTER THE LOCATION")
        ce = str(input("FROM STAION="))
        ceb = ce.upper()
        cee = str(input("TO STATION="))
        ceeb = cee.upper()
        print("YOUR TRAIN NAME IS=", ceeb, "SHADABADI EXPRESS")
        print("")
        num = random.randint(1000, 1100)
        print("THE TRAIN NO. IS=", num)
        print("YOUR TRAIN JOURNEY IS:", ceb, "TO", ceeb)
        d = str(input("DATE OF TRAIN RESERVATION [DD/MM/YYYY]="))
        de = d.upper()
        date.append(de)
        print("")
        print("SELECT THE CLASS YOU WOULD LIKE TO TRAVEL IN")
        print("""
		PRESS 1=FOR AC FIRST CLASS
		PRESS 2=FOR AC SECOND CLASS
		PRESS 3=FOR AC THIRD CLASS
		PRESS 4=SLPEER CLASS""")
        amount = "0"
        print("")
        e = str(input("ENTER THE TRAIN CLASS="))
        print("")
        # CONDITION 1
        if e == "1":
            print("ARE YOU SURE YOU TRAVEL IN AC FIRST CLASS")
            print("")
            amount = 1200 * ae
            for abcde1 in range(ae):
                pri1 = random.randint(1, 20)
                print("YOUR SEAT ACC. TO CLASS IS=", pri1)
            print("")
            print("YOUR TRAIN AMOUNT ACC. TO PASSENGER IS=", amount)
            pnr1 = random.randint(1500, 2100)
            print("YOUR PNR NUMBER IS=", pnr1)
            print("""
		IN WHICH METHOD YOU PAY THE AMOUNT
		PRESS 1=USING NET BANKING OR DEBIT CARD
		PRESS 2=E-WALLET
		PRESS 3=PAYMENT DONE BY UPI/BHIM
			""")
            ww = input("IN WHICH WAY YOU PAY THE AMOUNT=")
            print("")
            time.time
            a = time.asctime()
            print("THE TRAIN TICKET IS BOOKED ON", a)
            print("AND YOUR TRAIN IS ON", d)
            print("AT TIME 6:30 pm")
            if ae < 3:
                print("STATUS=TICKET IS CONFIRMED")
            else:
                print("STATUS=TICKET IS WAITING")
            print("")
            print("FOR MORE INFORMATION YOU GO TO OUR SITE TO SCAN THIS QR CODE")
            img = qrcode.make("https://www.irctc.co.in/nget/train-search")
            img.save("saved.png")
            img.show("saved.png")
        # CONDITION 2
        elif e == "2":
            print("ARE YOU SURE YOU TRAVEL IN AC SECOND CLASS")
            print("")
            amount = 1000 * ae
            for abcde2 in range(ae):
                pri2 = random.randint(60, 80)
                print("YOUR SEAT ACC. TO CLASS IS=", pri2)
            print("")
            print("YOUR TRAIN AMOUNT ACC. TO PASSENGER IS=", amount)
            pnr1 = random.randint(1500, 2100)
            print("YOUR PNR NUMBER IS=", pnr1)
            print("""
		IN WHICH METHOD YOU PAY THE AMOUNT
		PRESS 1=USING NET BANKING OR DEBIT CARD
		PRESS 2=E-WALLET
		PRESS 3=PAYMENT DONE BY UPI/BHIM
			""")
            ww = input("IN WHICH WAY YOU PAY THE AMOUNT=")
            print("")
            time.time
            a = time.asctime()
            print("THE TRAIN TICKET IS BOOKED ON", a)
            print("AND YOUR TRAIN IS ON", d)
            print("AT TIME 6:30 pm")
            if ae < 4:
                print("STATUS=TICKET IS CONFIRMED")
            else:
                print("STATUS=TICKET IS WAITING")
            print("")
            print("FOR MORE INFORMATION YOU GO TO OUR SITE TO SCAN THIS QR CODE")
            img = qrcode.make("https://www.irctc.co.in/nget/train-search")
            img.save("saved.png")
            img.show("saved.png")
        # CONDITION 3
        elif e == "3":
            print("ARE YOU SURE YOU TRAVEL IN AC THIRD CLASS")
            amount = 800 * ae
            print("")
            for abcde3 in range(ae):
                pri3 = random.randint(100, 125)
                print("YOUR SEAT ACC. TO CLASS IS=", pri3)
            print("")
            print("YOUR TRAIN AMOUNT ACC. TO PASSENGER IS=", amount)
            pnr1 = random.randint(1500, 2100)
            print("YOUR PNR NUMBER IS=", pnr1)
            print("""
		IN WHICH METHOD YOU PAY THE AMOUNT
		PRESS 1=USING NET BANKING OR DEBIT CARD
		PRESS 2=E-WALLET
		PRESS 3=PAYMENT DONE BY UPI/BHIM
			""")
            ww = input("IN WHICH WAY YOU PAY THE AMOUNT=")
            print("")
            time.time
            a = time.asctime()
            print("THE TRAIN TICKET IS BOOKED ON", a)
            print("AND YOUR TRAIN IS ON", d)
            print("AT TIME 6:30 pm")
            if ae < 5:
                print("STATUS=TICKET IS CONFIRMED")
            else:
                print("STATUS=TICKET IS WAITING")
            print("")
            print("FOR MORE INFORMATION YOU GO TO OUR SITE TO SCAN THIS QR CODE")
            img = qrcode.make("https://www.irctc.co.in/nget/train-search")
            img.save("saved.png")
            img.show("saved.png")
        # CONDITION 4
        elif e == "4":
            print("ARE YOU SURE YOU TRAVEL IN SLEEPER CLASS")
            amount = 500 * ae
            print("")
            for abcde4 in range(ae):
                pri4 = random.randint(130, 160)
                print("YOUR SEAT ACC. TO CLASS IS=", pri4)
            print("")
            print("YOUR TRAIN AMOUNT ACC. TO PASSENGER IS=", amount)
            pnr1 = random.randint(1500, 2100)
            print("YOUR PNR NUMBER IS=", pnr1)
            print("""
		IN WHICH METHOD YOU PAY THE AMOUNT
		PRESS 1=USING NET BANKING OR DEBIT CARD
		PRESS 2=E-WALLET
		PRESS 3=PAYMENT DONE BY UPI/BHIM
			""")
            ww = input("IN WHICH WAY YOU PAY THE AMOUNT=")
            print("")
            time.time
            a = time.asctime()
            print("THE TRAIN TICKET IS BOOKED ON", a)
            print("AND YOUR TRAIN IS ON", d)
            print("AT TIME 6:30 pm")
            if ae < 5:
                print("STATUS=TICKET IS CONFIRMED")
            else:
                print("STATUS=TICKET IS WAITING")
            print("")
            print("FOR MORE INFORMATION YOU GO TO OUR SITE TO SCAN THIS QR CODE")
            img = qrcode.make("https://www.irctc.co.in/nget/train-search")
            img.save("saved.png")
            img.show("saved.png")
        # ELSE PART
        else:
            print("INVALID STATEMENT THESE OPTION IS NONE OF THE ABOVE ")
            print("RE-RUN THE PROGRAM")
    except:
        print("")
        print("ONLY ENTER NUMERIC VALUE IN PASSENGER COLUMN")
        print("RE-RUN THE PROGRAM ")
    print("\n" * 4)
    print("           =============RESTART================")


# FUNCTION OF CHECK THE DETAILS
def checkdetail():
    print("")
    print("       ============CHECK THE TRAIN DETAILS=============")
    print("")
    ab = input("ENTER THE TRAIN NUMBER=")
    try:
        abcc = int(ab)
        if 1000 <= abcc <= 1100:
            print("YOUR TRAIN NUMBER IS VALID")
            print("")
            abbbbb = input("ENTER THE NAME OF TRAIN=")
            abb = input("ENTER THE PNR NUMBER=")
            try:
                abbc = int(abb)
                if 1500 <= abbc <= 2100:
                    print("YOUR PNR NUMBER IS RIGHT")
                    print("")
                    abbb = input("ENTER THE DATE OF TRAIN=")
                    abbbb = input("NUMBER OF PASSENGERS=")
                    print("YOUR TRAIN IS ON DATE=", abbb)
                    print("YOUR STATUS=TICKET IS CONFIRMED")
                    print("")
                    print("FOR MORE DETAILS YOU LOGIN TO OUR SITE TO SCAN THIS QR CODE")
                    img = qrcode.make("https://www.irctc.co.in/nget/train-search")
                    img.save("saved.png")
                    img.show("saved.png")
                else:
                    print("YOUR PNR NUMBER IS INVALID")
            except:
                print("")
                print("PLS ENTER NUMERIC VALUE IN PNR NUMBER COLUMN")
                print("RE-RUN THE PROGRAM")
        else:
            print("SORRY THIS TRAIN NUMBER IS NOT VALID RE-RUN THE PROGRAM")
    except:
        print("")
        print("PLS ENTER NUMERIC VALUE IN TRAIN NUMBER COLUMN")
        print("RE-RUN THE PROGRAM")
    print("\n" * 4)
    print("           =============RESTART================")


# ABOUT THE PROGRAM
def aboutprogram():
    print("")
    print("         ===============ABOUT PROGRAM===============")
    print("""
	1)TASK = TRAIN RESERVATION SYSTEM
	2)TASK COMPLETED BY = UJJWAL SAINI & NITIN
	3)TASK GIVEN BY = VIKAS SHARMA {SIR}
	4)PRINCIPAL NAME = MRS.PREETI SHUKLA
	5)PROGRAM DESIGN BY = UJJWAL SAINI
	6)SCHOOL = S.B.MILLS SER.SECONDARY SCHOOL
	7)PROGRAMMING LANGUAGE USED = PYTHON IDE AND MY SQL[FOR DATABASE]
	8)CLASS = 11th B""")
    print("\n" * 4)
    print("           =============RESTART================")


# FUNCTION TO EDIT THE PROFILE
def editprofile():
    print("")
    print("      ===============EDIT THE PROFILE ===============")
    print("""
	IN THESE OPTION WHICH ONE IS YOU EDIT
	PRESS 1=NUMBER OF PASSENGER
	PRESS 2=THE LOCATION
	        1)FROM STATION
	        2)TO STATION
	PRESS 3=DATE OF TRAIN RESERVATION
	""")

    # FUNCTION FOR PASSENGER NUMBER
    def numberpassenger():
        a1 = input("ENTER THE PREVIOUSLY NUMBER OF PASSENGER=")
        print("")
        a2 = input("ENTER THE NUMBER OF PASSENGER=")
        try:
            passen.remove(a1)
            passen.append(a2)
            print("YOUR NUMBER OF PASSENGER SUCCESSFULLY REGISTER")
        except:
            print("")
            print("THIS NUMBER OF PASSENGER ARE NOT IN OUR SERVER LIST")
            print("PLS RE-RUN THE PROGRAM WITH NEW RESERVATION OF TRAIN AGAIN")
            print("SORRY!!!")

    # FUNCTION FOR LOCATION
    def thelocation():
        print("""
	PRESS 1=FROM STATION
	PRESS 2=TO STATION""")
        a3 = input("ENTER THE CHOICE=")
        if a3 == "1":
            a41 = input("ENTER THE PREVIOUS LOCATION=")
            a4 = a41.upper()
            a441 = input("ENTER THE NEW LOCATION=")
            a44 = a441.upper()
            local.append(a44)
            print("YOUR LOCATION IS SUCCESSFULLY REGISTER ")
        elif a3 == "2":
            a51 = input("ENTER THE PREVIOUS LOCATION=")
            a5 = a51.upper()
            a551 = input("ENTER THE NEW LOCATION=")
            a55 = a551.upper()
            local.append(a55)
            print("YOUR LOCATION IS SUCCESSFULLY REGISTER ")
        else:
            print("INVALID CHOICE")

    # FUNCTION FOR DATE
    def traindate():
        a61 = input("ENTER THE PREVIOUS DATE=")
        a6 = a61.upper()
        a661 = input("ENTER THE NEW DATE=")
        a66 = a661.upper()
        date.append(a66)
        print("THE DATE IS SUCCESSFULLY ADDED")

    aaaa = input("ENTER THE CHOICE WHICH YOU EDIT=")
    if aaaa == "1":
        numberpassenger()
    elif aaaa == "2":
        thelocation()
    elif aaaa == "3":
        traindate()
    else:
        print("INVALID CHOICE")
    print("\n" * 4)
    print("           =============RESTART================")


# FUNCTION OF CANCELLATION OF THE TICKET
def cancelticket():
    print("")
    print("       ===========CANCELLATION OF TICKET============")
    print("")
    aa1 = input("ENTER THE NUMBER OF PASSENGER=")
    try:
        aa11 = int(aa1)
        if aa11 <= 3:
            amount1 = 1000 * aa11  # 75% refund
            am1 = 75 * amount1 / 100
        elif 4 <= aa11 <= 6:
            amount11 = 1100 * aa11  # 50% refund
            am2 = 50 * amount11 / 100
        else:
            amount111 = 1200 * aa11  # 40% refund
            am3 = 40 * amount111 / 100
        print("")
        print("ENTER THE LOCATION ")
        ab1 = input("FROM STAION=")
        abb1 = input("TO STATION=")
        print("")
        ac1 = input("ENTER THE NAME OF TRAIN=")
        ad1 = input("DATE OF TRAIN RESERVATION [DD/MM/YYYY]=")
        print("")
        ae11 = input("ENTER THE PNR NUMBER=")
        try:
            ae1 = int(ae11)
            if 1500 <= ae1 <= 2000:
                print("YOUR PNR NUMBER IS CORRECT")
                print("")
                print("YOUR RESERVATION IS SUCCESSFULLY CANCEL")
                if aa11 <= 3:
                    print("YOUR AMOUNT WILL BE REFUNDED=", am1)
                    print("OUT OF AMOUNT=", amount1)
                elif 4 <= aa11 <= 6:
                    print("YOUR AMOUNT WILL BE REFUNDED=", am2)
                    print("OUT OF AMOUNT=", amount11)
                else:
                    print("YOUR AMOUNT WILL BE REFUNDED=", am3)
                    print("OUT OF AMOUNT=", amount111)
            else:
                print("RE-RUN THE PROGRAM")
                print("YOUR PNR NUMBER IS INVALID")
        except:
            print("")
            print("PLS ENTER NUMERIC VALUE IN PNR COLUMN")
    except:
        print("")
        print("PLS ENTER NUMERIC VALUE IN PASSENGER COLUMN")
        print("RE-RUN THE PROGRAM")
    print("\n" * 4)
    print("           =============RESTART================")


# FUNCTION TO EXIT THE PROGRAM
def exit1():
    print("")
    print("        ===========TO EXIT THE PROGRAM =============")
    print("")
    q11 = input("ARE YOU SURE YOU EXIT THE PROGRAM [Y/N]=")
    q1 = q11.upper()
    if q1 == "Y" and "YES":
        exit()
    elif q1 == "N" and "NO":
        print("")
        print("MEANS YOU RE-RUN THE PROGRAM")
    else:
        print("INVALID CHOICE ")
    print("\n" * 4)
    print("           =============RESTART================")


# FUNCTION OF TRAIN MENU
def railmenu():
    print("")
    print("         ============ TRAIN RESERVATION =============")
    print("THIS PROGRAM IS FOR TRAIN RESERVATION")
    print("""        THESE ARE SIX OPTION :
	PRESS 1=FOR RESERVATION OF TICKET
	PRESS 2=TO CHECK THE DETAILS OF TRAIN
	PRESS 3=TO EDIT YOUR PROFILE OF TRAIN TICKET
	PRESS 4=TO CANCEL THE TICKET
	PRESS 5=ABOUT PROGRAM
	PRESS 6=TO EXIT THE PROGRAM
	""")
    abcd = str(input("ENTER YOUR CHOICE="))
    if abcd == "1":
        reservationticket()
    elif abcd == "2":
        checkdetail()
    elif abcd == "3":
        editprofile()
    elif abcd == "4":
        cancelticket()
    elif abcd == "5":
        aboutprogram()
    elif abcd == "6":
        exit1()
    else:
        print("INVALID CHOICE")


railmenu()
# FOR RE-RUN THE PROGRAM
for i in range(100):
    print("")
    xyz1 = str(input("YOU WANT TO RUN THE PROGRAM AGAIN [Y/N]="))
    xyz = xyz1.upper()
    if xyz == "Y" and "YES":
        railmenu()
    elif xyz == "N":
        exit()
    else:
        print("WRONG CHOICE")
print("")
