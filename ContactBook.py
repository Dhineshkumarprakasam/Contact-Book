import sqlite3
import os
import time
import pyfiglet

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

class add:
    def __init__(self):
        while(True):
            try:
                clear_screen()
                print("** Add New Contact **")
                name = input("Enter Contact Name : ")
                phone = int(input("Enter Mobile Number : "))
                if(len(str(phone))!=10):
                    raise ValueError
                break
            except ValueError or TypeError :
                clear_screen()
                print("-->Oops, you have typo<--")
                time.sleep(1)
                continue

        clear_screen()

        cursor.execute("INSERT INTO DETAILS VALUES(?,?)",(name,phone))
        con.commit()

        print("** Successfully Saved Contact **")
        print("Name  : ",name)
        print("Phone : ",phone)

        time.sleep(2)
        clear_screen()


class view:
    def viewAll(self):
        cursor.execute("SELECT * FROM DETAILS ORDER BY NAME")
        data = cursor.fetchall()
        for name, phone in data:
            print(f"Name  : {name}")
            print(f"Phone : {phone}\n")
        ex=input("Press Enter to exit")
        clear_screen()
    
    def viewByName(self):
        findName=input("Enter Name to find : ")
        found=0
        cursor.execute("SELECT * FROM DETAILS")
        data = cursor.fetchall()
        for name, phone in data:
            if(findName==name):
                print(f"\nName  : {name}")
                print(f"Phone : {phone}")
                found=1
                break
        if(found==0):
            print("--> Oops, Contact not found <--")
            time.sleep(1)
            clear_screen()
            self.__init__()
        else:
            ex=input("\nPress Enter to exit")
            clear_screen()
    
    def viewByNumber(self):
        findNumber=input("Enter Number to find : ")
        found=0
        cursor.execute("SELECT * FROM DETAILS")
        data = cursor.fetchall()
        for name, phone in data:
            if(findNumber==str(phone)):
                print(f"\nName  : {name}")
                print(f"Phone : {phone}")
                found=1
                break
        if(found==0):
            print("--> Oops, Contact not found <--")
            time.sleep(1)
            clear_screen()
            self.__init__()
        else:
            ex=input("\nPress Enter to exit")
            clear_screen()
                

    def __init__(self):
        while(True):
            try:
                clear_screen()
                print("** View Contact **")
                print("0.Exit \n1.All \n2.Search By Name \n3.Search By Number")
                self.choice = int(input("Enter your choice : "))

                if(self.choice==0):
                    clear_screen()

                elif(self.choice==1):
                    clear_screen()
                    self.viewAll()

                elif(self.choice==2):
                    clear_screen()
                    self.viewByName()
                
                elif(self.choice==3):
                    clear_screen()
                    self.viewByNumber()

                else:
                    clear_screen()
                    print("-->Oops, Try entering correct choice<--")
                    time.sleep(1)
                    clear_screen()
                    continue

                break
            except ValueError or TypeError:
                continue
            
class update:
    def updateNumber(self):
        findName=input("Enter Name to find : ")
        found=0
        cursor.execute("SELECT * FROM DETAILS")
        data = cursor.fetchall()
        for name, phone in data:
            if(findName==name):
                while(True):
                    try:
                        clear_screen()
                        self.newPhone = int(input("Enter New Mobile Number : "))
                        if(len(str(phone))!=10):
                            raise ValueError
                        break
                    except ValueError or TypeError :
                        clear_screen()
                        print("-->Oops, you have typo<--")
                        time.sleep(1)
                        continue
                cursor.execute("UPDATE DETAILS SET PHONE = ? WHERE NAME = ?",(self.newPhone,findName))
                con.commit()
                clear_screen()
                print("**Success fully Updated**")

                found=1
                break
        if(found==0):
            print("--> Oops, Contact not found <--")
            time.sleep(1)
            clear_screen()
            self.__init__()
        else:
            ex=input("\nPress Enter to exit")
            clear_screen()

    
    def __init__(self):
        while(True):
            try:
                clear_screen()
                print("** Update Contact **")
                print("0.Exit \n1.Update Number")
                self.choice = int(input("Enter your choice : "))

                if(self.choice==0):
                    clear_screen()
                    
                elif(self.choice==1):
                    clear_screen()
                    self.updateNumber()

                else:
                    clear_screen()
                    print("-->Oops, Try entering correct choice<--")
                    time.sleep(1)
                    clear_screen()
                    continue
                
                break
            except ValueError or TypeError:
                continue

class delete:
    def deleteByName(self):
        findName=input("Enter Name to find : ")
        found=0
        cursor.execute("SELECT * FROM DETAILS")
        data = cursor.fetchall()
        for name, phone in data:
            if(findName==name):
                cursor.execute("DELETE FROM DETAILS WHERE NAME = ?",(findName,))
                con.commit()
                print("**Success fully Deleted**")
                print(f"\nName  : {name}")
                print(f"Phone : {phone}")
                found=1
                break
        if(found==0):
            print("--> Oops, Contact not found <--")
            time.sleep(1)
            clear_screen()
            self.__init__()
        else:
            ex=input("\nPress Enter to exit")
            clear_screen()
    
    def deleteByNumber(self):
        findNumber=input("Enter Number to find : ")
        found=0
        cursor.execute("SELECT * FROM DETAILS")
        data = cursor.fetchall()
        for name, phone in data:
            if(findNumber==str(phone)):
                cursor.execute("DELETE FROM DETAILS WHERE PHONE = ?",(findNumber,))
                con.commit()
                print("**Success fully Deleted**")
                print(f"\nName  : {name}")
                print(f"Phone : {phone}")
                found=1
                break
        if(found==0):
            print("--> Oops, Contact not found <--")
            time.sleep(1)
            clear_screen()
            self.__init__()
        else:
            ex=input("\nPress Enter to exit")
            clear_screen()
    
    def __init__(self):
        while(True):
            try:
                clear_screen()
                print("** Delete Contact **")
                print("0.Exit \n1.Delete By Name \n2.Delete By Number")
                self.choice = int(input("Enter your choice : "))

                if(self.choice==0):
                    clear_screen()

                elif(self.choice==1):
                    clear_screen()
                    self.deleteByName()

                elif(self.choice==2):
                    clear_screen()
                    self.deleteByNumber()

                else:
                    clear_screen()
                    print("-->Oops, Try entering correct choice<--")
                    time.sleep(1)
                    clear_screen()
                    continue
                
                break
            except ValueError or TypeError:
                continue


#connecting to database
con = sqlite3.connect("contactBookApplication.db")
cursor = con.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS DETAILS(NAME VARCHAR(50), PHONE BIGINT)")

#main program
t1 = pyfiglet.figlet_format("Welcome")
t2 = pyfiglet.figlet_format("           TO")
t3 = pyfiglet.figlet_format("Contact Book")

print(t1)
print(t2)
print(t3)
print("Loading...")
time.sleep(3)


clear_screen()
while(True):
    print("0.Exit \n1.Add \n2.View \n3.Update \n4.Delete ")
    choice = int(input("Enter your choice : "))

    if(choice==0):
        con.close()
        clear_screen()
        t4=pyfiglet.figlet_format("Thank You")
        print(t4)
        print("Exiting..")
        time.sleep(3)
        break

    elif(choice==1):
        obj=add()

    elif(choice==2):
        obj=view()

    elif(choice==3):
        obj=update()
    
    elif(choice==4):
        obj=delete()
    
    else:
        clear_screen()
        print("-->Oops, Try entering correct choice<--")
        time.sleep(1)
        clear_screen()
        continue
    




