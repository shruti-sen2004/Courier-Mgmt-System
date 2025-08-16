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