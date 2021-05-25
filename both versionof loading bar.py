
import sys

print("CLICK 1 IF YOU USE OLD VERSION \nCLICK 2 IF YOU USE LATEST VERSION")
print("")
a=str(input("ENTER YOUR CHOICE="))
# OLD VERSION OF LOADING BAR
if a == "1" :
    print("LOADING.....")
    from time import sleep
    for i in range(100):
        sleep(0.12)
    print("hello")

# LATEST VERSION OF LOADING BAR [TQDM]

if a == "2":
    print("YOU USE LATEST VERSION OF LOADING BAR")
    from tqdm import tqdm
    
    for i in tqdm(range(8)):
        print()
    
