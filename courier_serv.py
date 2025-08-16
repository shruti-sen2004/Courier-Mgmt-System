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
    print("\n\n Designed by: Shruti Sen \n\n")
    Disp_star(60)
    x=input("\n\t\t\tPress enter key to continue....")

def Cust_Menu():
    while(1):
        print("\n\n\n\n")
        Disp_star(60)
        print("\n\t\t\t CUSTOMER MENU\n\n\n")
        print("\t1. Register a New Customer")
        print("\t2. Login")
        print("\t3. Return to Main Menu")

        ch=int(input("\n\n\tEnter your choice(1-3): "))
        if ch==1:
            Cust_Register()
        elif ch==2:
            Cust_Login()
        elif ch==3:
            break

def Cust_Register():
    createTable ="""CREATE TABLE IF NOT EXISTS customer_account_details(Name char(50) NOT NULL,
    User_ID char(15) NOT NULL,Password char(15) NOT NULL)"""
    cursor.execute(createTable)
    
    name=input("Enter your name : ")
    user_id=input("Enter a User ID : ")
    password=input("Enter a password :")
    st="INSERT INTO customer_account_details(Name,User_ID,Password) VALUES ('{}','{}','{}')".format(name,user_id,password)
    cursor.execute(st)
    mycon.commit()
    print("You are registered.  ")

def Cust_Login():
    print("Enter the details for login")
    u_id=input("Enter your User ID : ")
    psw=input("Enter the password :")
    sql="SELECT * FROM Customer_Account_Details WHERE User_ID = %s and Password=%s"
    values=(u_id,psw)
    data=cursor.execute(sql,values)
    data=cursor.fetchone()      

    if data != None:
        print("YOU HAVE BEEN SUCCESSFULLY LOGGED IN!!!!")
        while True:
            print("\n\n\n\n")
            Disp_star(60)
            
            print("\n\t\t\t PARCEL MENU\n\n\n")
            print("\t1. Parcel Delivery Details")
            print("\t2. Bill")
            print("\t3. Return to Customer Menu")
        
            ch=int(input("\n\n\tEnter your choice(1-3): "))
            if ch==1:
                print("delivery details")
            elif ch==2:
                print("print bill")
            elif ch==3:
                break
            else:
                print("Invalid input. Try again!!!!!")
    else:
        print("WRONG USER ID OR PASSWORD!!!")

def mainMenu():
    while(1):
        print("\n\n\n\n")
        Disp_star(60)
        print("\n\t\t\t MAIN MENU\n\n")
        print("\t1. Customer")
        print("\t2. Employee")
        print("\t3. Exit")

        ch=int(input("\n\n\tEnter your choice(1-3): "))
        if ch==1:
            Cust_Menu()
        elif ch==2:
            print("Emp_Menu()")
        elif ch==3:
            txt="THANK YOU. VISIT AGAIN."
            print("\n\n\t",end="")
            for i in range(len(txt)):
                print(txt[i], end=" ")
                #time.sleep(0.1) 
            break
        else:
            print("Invalid input. Try again!!!!!")

welcome()
mainMenu()