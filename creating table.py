from prettytable import PrettyTable

# table from the list
list1=[" "," "," "," "," "," "," "]
list2=[" "," "," "," "," "," "," "]
list3=[" "," "," "," "," "," "," "]

# USE COURIER NEW FONT FOR BEST TABLE CONTENT
table = PrettyTable([" 1 "," 2 "," 3 "])
for x in range(0,6):
    table.add_row ([list1[x],list2[x],list3[x]])
print(table)
