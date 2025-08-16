import time
import mysql.connector as ms

mycon=ms.connect(host="localhost",user="root",password="",database="c_m_system")

if mycon.is_connected():
    print("Successful")

cursor=mycon.cursor()

def Disp_star(x):
    for i in range(x):
        print("*", end="")

def welcome():
    Disp_star(60)
    print("\n\t WELCOME TO LIGHTYEAR COURIER EXPRESS SERVICE")
    print("\n\n  Designed by:\n\t\t Shruti Sen")
    print("\n\n\n")
    Disp_star(60)
    x=input("\n\t\t\tPress enter key to continue....")

def mainMenu():
    while(1):
        print("\n\n\n\n")
        Disp_star(60)
        print("\n\t\t\t MAIN MENU\n\n\n")
        print("\t1. Customer")
        print("\t2. Employee")
        print("\t3. Exit")

        ch=int(input("\n\n\tEnter your choice(1-3): "))
        if ch==1:
            print("Cust_Menu()")
        elif ch==2:
            print("Emp_Menu()")
        elif ch==3:
            txt="THANK YOU. VISIT AGAIN."
            print("\n\n\n\n\t",end="")
            for i in range(len(txt)):
                print(txt[i], end=" ")
                #time.sleep(0.1) 
            break
        else:
            print("Invalid input. Try again!!!!!")

welcome()
mainMenu()