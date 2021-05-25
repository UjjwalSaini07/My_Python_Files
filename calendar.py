import calendar
for i in range(100):
	print("""ENTER YOUR CHOICE 
	PRESS 1 = IF YOU SEE CALENDAR OF WHOLE THE YEAR
	PRESS 2 = IF YOU SEE CALCENDAR MONTH WISE""")
	a=str(input("ENTER YOUR CHOICE="))
	if a=="1":
		print("           YOU SEE THE CALENDAR OF WHOLE THE YEAR")
		year=int(input("ENTER THE YEAR="))
		calendar.setfirstweekday(6)
		m=calendar.calendar(year)
		print("THE YEAR IS=",year)
		print("")
		print(m)
		print("")
		print("GOODBYE")
	if a=="2":
		print("             YOU SEE CALCENDAR MONTH WISE")
		year=int(input("ENTER THE YEAR="))
		month=int(input("ENTER THE MONTH [IN NUMBER]="))
		calendar.setfirstweekday(Sunday)
		yr=calendar.month(year,month)
		print("")
		print("THIS IS THE CALENDAR OF MONTH=",month,"\n","THE YEAR IS=",year)
		print("")
		print(yr)
		print("")
		print("GOODBYE")
	else:
		print("INVALID STATEMENT","\n","RE-RUN THE PROGRAM")
		print("GOODBYE")
