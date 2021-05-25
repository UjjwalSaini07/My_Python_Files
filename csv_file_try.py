import csv
file_check = open("create_a_file.csv","w")
create_writer = csv.writer(file_check)
create_writer.writerow(["NAME","AGE","GENDER"])
for i in range(4):
    print("STUDENT RECORD",i+1)
    name = input("ENTER YOUR NAME HERE = ")
    age = int(input("ENTER YOUR AGE = "))
    gender = input("ENTER YOUR GENDER = ")
    print("")
    create_rec = [name,age,gender]
    create_writer.writerow(create_rec)

create_writer.writerow(["HEIGHT"])
height =input("ENTER YOUR HEIGHT HER = ")
create_rec = [height]
create_writer.writerow(create_rec)

file_check.close()
