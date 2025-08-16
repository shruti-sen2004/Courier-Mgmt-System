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

def Emp_Menu():
    loginid="EMD0002"
    psw="4321"
    logid=input("Enter Employee ID: ")
    pw=input("Enter Password: ")

    if logid==loginid and pw==psw:
        while(1):
            print("\n\n\n\n")
            Disp_star(60)
            print("\n\t\t\t EMPLOYEE MENU\n\n\n")
            print("\t1. Add customer details")
            print("\t2. Add Dispatch details")
            print("\t3. Return to main menu")

            ch=int(input("\n\n\tEnter your choice(1-3): "))
            if ch==1:
                Cust_pack_details()
            elif ch==2:
                Dispatch_details()
            elif ch==3:
                break
            else:
                print("Invalid input. Try again!!!!!")
    else:
        print("WRONG USER ID OR PASSWORD!!!")

def Cust_pack_details():
    createTable ="""CREATE TABLE IF NOT EXISTS parcel(parcel_id int auto_increment PRIMARY KEY,p_date date NOT NULL,
    Sname char(50) NOT NULL,saddr char(50) NOT NULL,smob char(15) NOT NULL,Rname char(30)
    NOT NULL, raddr char(50) NOT NULL, rmob char(15),p_wt_kg smallint NOT NULL,amount smallint NOT NULL)"""
    cursor.execute(createTable)

    print('*' * 40)
    print(" ENTER CUSTOMER DETAILS ")
    print('*' * 40)
    print("\n\n")
    parcel_date=input("ENTER THE DATE: ")
    sender_name=input("ENTER SENDER'S NAME:")
    sender_address=input("ENTER SENDER'S ADDRESS:")
    sender_mobile=input("ENTER SENDER'S MOBILE NO.:")
    receiver_name=input("ENTER RECIEVER'S NAME:")
    receiver_addr=input("ENTER RECIEVER'S ADDRESS:" )
    receiver_mobile=input("ENTER RECIEVER'S MOBILE NO.: ")
    parcel_wt=input("ENTER PARCEL WEIGHT IN kg: ")
    amount=float(input("ENTER THE TOTAL AMOUNT="))
    st="""INSERT INTO parcel(p_date,Sname,saddr,smob,Rname,raddr,rmob,p_wt_kg,amount)
             VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}')""".format(parcel_date,sender_name,sender_address,sender_mobile,receiver_name,receiver_addr,receiver_mobile,parcel_wt,amount)
    cursor.execute(st)
    mycon.commit()
    print("\n\n")
    print("One record is added successfully !!!!!")
    

def Dispatch_details():
    createTable ="""CREATE TABLE IF NOT EXISTS dispatch(parcel_id int auto_increment PRIMARY KEY,d_boy_id varchar(5),pin_deliv bigint,
                    dsc_1 varchar(30),mot_1 char(10), dsc_2 varchar(30), mot_2 char(10),
                    dsc_3 varchar(30), mot_3 char(10))"""
    cursor.execute(createTable)

    print('*' * 40)
    print(" ENTER DISPATCH DETAILS ")
    print('*' * 40)
    print("\n\n")
    delivery_boy_id=input("ENTER THE DELIVERY BOY ID: ")
    delivery_pincode=input("ENTER DELIVERY PINCODE:")
    dispatch_1=input("ENTER FIRST DISPATCH CENTRE:")
    transport_1=input("ENTER FIRST MODE OF TRANSPORT:")
    dispatch_2=input("ENTER SECOND DISPATCH CENTRE(if any):")
    transport_2=input("ENTER SECOND MODE OF TRANSPORT(if any):")
    dispatch_3=input("ENTER THIRD DISPATCH CENTRE(if any):")
    transport_3=input("ENTER THIRD MODE OF TRANSPORT(if any):")
    st="""INSERT INTO dispatch(d_boy_id,pin_deliv,dsc_1,mot_1,dsc_2,mot_2,dsc_3,mot_3)
             VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')""".format(delivery_boy_id,delivery_pincode,dispatch_1,transport_1,dispatch_2,transport_2,dispatch_3,transport_3)
    cursor.execute(st)
    mycon.commit()
    print("\n\n")
    print("One record is added successfully !!!!!")


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