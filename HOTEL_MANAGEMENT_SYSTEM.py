# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 11:41:54 2022

@author: WIN--10
"""

print("\n","~"*50,"\n\n\t   WELCOME TO THE GREAT GRAND HOTEL  ","\n","~"*50)
import mysql.connector
hotel=mysql.connector.connect(host="localhost",user="root",passwd="mridul_mysql",database="hotel")
cursor=hotel.cursor()

while True:
    a= int(input('''\t1. ADD NEW ROOM
             \n\t2. ADD CUSTOMER
             \n\t3. MODIFY ROOM INFORMATION
             \n\t4. MODIFY CUSTOMER INFORMATION
             \n\t5. ROOM BOOKING
             \n\t6. BILL GENERATION
             \n\t7. DELETE A CUSTOMER RECORD
             \n\t8. SETTINGS
             \n\t9. EXIT.
             \nChoice ~'''))

    if a == 1:
        while True:
            print("\tEXISTING ROOMS :\n")
            cursor.execute("Select * from rooms;")
            data=cursor.fetchall()
            for i in data:
                print(i)
            print("\n")
            roomno=int(input("Enter the Room No. :- "))   
            roomtype=input("Enter room Type :- ")
            roomrent=float(input("Enter Room rent :-"))
            roombed=input("Enter Bed Type :-" )
            status=input("Status :-")
            cursor.execute("INSERT INTO rooms (ROOM_NO,ROOM_TYPE,ROOM_RENT,ROOM_BED,STATUS) VALUES ({},'{}',{},'{}','{}');".format(roomno,roomtype,roomrent,roombed,status))
            cursor.execute("Commit;")
            print("****Data inserted successfully......*****")
            x=int(input(" 1 ---> Enter data\n 2 ---> Exit\n \t CHOICE :~ "))
            if x>2 or x<1:
                print("CHOOSE EITHER 1 or 2")
            if x==2:
                break
            print("\n","_"*25,"\n\n\t    MAIN MENU    ","\n","_"*25)
        
            
    if a == 2:
        while True:
            name=input("Enter your name :")
            address=input("Enter your residence Address :")
            emailid=input("Enter your email_id :")
            idproof=input("Enter the id proof name :")
            idproofno=input("Enter the id proof number :")
            males=int(input("Enter the no. of males :"))
            females=int(input("Enter the no. of females :"))
            children=int(input("Enter the no. of children :"))
            phone=int(input("Enter your phone no. :"))
            cursor.execute("INSERT INTO CUSTOMER (NAME,ADDRESS,EMAIL_ID,ID_PROOF,ID_PROOF_NO,MALES,FEMALES,CHILDREN,PHONE) VALUES ('{}','{}','{}','{}','{}',{},{},{},{});".format(name,address,emailid,idproof,idproofno,males,females,children,phone))
            cursor.execute("commit;")
            print("DATA SUCCESSFULLY INSERTED....")
      
            x=int(input(" 1 ---> Enter data\n 2 ---> Exit\n \t CHOICE :~ "))
            if x==2 :
                break
            print("\n","_"*25,"\n\n\t    MAIN MENU    ","\n","_"*25)
    if a == 3:
        while True:
            y=int(input('''1 ---> Show Room Data to Find Room ID.
                    \n\n2 ---> Update the Data.
                    \n\n3 ---> EXIT.
                    \n\n\t\t CHOICE:'''))
            print('='*50)
            if y == 3:
                break
            elif y == 1:
                cursor.execute("Select * from rooms;")
                data=cursor.fetchall()
                for i in data:
                    print("\nRoom ID:-\t",i[0],"\nRoom No.:-\t",i[1],"\nRoom Type:-",i[2],"\nRoom Rent:-\t",i[3],"\nRoom Bed:-\t",i[4],"\nRoom Status:-\t",i[5])
                
            elif y == 2:
                roomid=int(input("Enter the Room ID :- "))   
                roomno=int(input("Enter the Room No. :- "))   
                roomtype=input("Enter room Type :- ")
                roomrent=float(input("Enter Room rent :- Rs."))
                roombed=input("Enter Bed Type :-" )
                status=input("Status :-")
                query1="Update rooms set room_no = {} where id={};".format(roomno,roomid)
                query2="Update rooms set room_type = '{}' where id={};".format(roomtype,roomid)
                query3="Update rooms set room_rent= {} where id={};".format(roomrent,roomid)
                query4="Update rooms set room_bed= '{}' where id={};".format(roombed,roomid)
                query5="Update rooms set status='{}' where id={};".format(status,roomid)
                cursor.execute(query1)
                cursor.execute(query2)
                cursor.execute(query3)
                cursor.execute(query4)
                cursor.execute(query5)
                cursor.execute("Commit;")
                print("DATA SUCCESSFULLY UPDATED......")
                x=int(input(" 1 ---> Update more data\n 2 ---> Exit\n \t CHOICE :~ "))
                if x==2 :
                    break
                print("\n","_"*25,"\n\n\t    MAIN MENU    ","\n","_"*25)
    if a == 4:
        
        while True:
            z=int(input('''1 ---> Update Name.
            \n2 ---> Update Email ID.
            \n3 --->Update Phone no.
            \n4 ---> EXIT.\n\t CHOICE :~'''))
            if z==1:
                name=input("Customer's name: ")   
                cursor.execute("Select id,name,phone from customer where name like '%{}%';".format(name))
                data1=cursor.fetchall()
                print("\n","_"*50,"\n\n\t   DISPLAYING CUSTOMER DATA TO FIND CUST_ID   ","\n","_"*50)
                for a in data1:
                    print(" ID :- ",a[0],"\n Name :-",a[1],"\n Phone no.",a[2])
                    print("_"*30)
                print("\n")       
                id=input("Enter the customer ID:~ ")
                name=input("Update your name :~ ")
                cursor.execute("UPDATE CUSTOMER set name = '{}' where id={};".format(name,id)) 
                print("NAME UPDATED SUCCESSFULLY ...")
                x=int(input(" 1 ---> Update once more.\n 2 ---> Exit\n \t CHOICE :~ "))
                if x==2 :
                    break
            if z==2:  
                name=input("Customer's name: ")   
                cursor.execute("Select id,name,phone from customer where name like '%{}%';".format(name))
                data1=cursor.fetchall()
                print("\n","_"*50,"\n\n\t   DISPLAYING CUSTOMER DATA TO FIND CUST_ID   ","\n","_"*50)
                for a in data1:
                    print(" ID :- ",a[0],"\n Name :-",a[1],"\n Phone no.",a[2])
                    print("_"*30)
                print("\n")       
                id=input("Enter the customer ID:~ ")
                emailid=input("Enter your email_id :")
                cursor.execute("UPDATE CUSTOMER set EMAIL_ID = '{}' where id={};".format(emailid,id)) 
                print("EMAIL_ID UPDATED SUCCESSFULLY ...")
                x=int(input(" 1 ---> Update once more.\n 2 ---> Exit\n \t CHOICE :~ "))
                if x==2 :
                    break
                
            if z==3:
                name=input("Customer's name: ")   
                cursor.execute("Select id,name,phone from customer where name like '%{}%';".format(name))
                data1=cursor.fetchall()
                print("\n","_"*50,"\n\n\t   DISPLAYING CUSTOMER DATA TO FIND CUST_ID   ","\n","_"*50)
                for a in data1:
                    print(" ID :- ",a[0],"\n Name :-",a[1],"\n Phone no.",a[2])
                    print("_"*30)
                print("\n")       
                id=input("Enter the customer ID:~ ")
                phone=int(input("Enter your phone no. :"))
                cursor.execute("UPDATE CUSTOMER set PHONE = '{}' where id={};".format(phone,id))
                print("PHONE NUMBER UPDATED SUCCESSFULLY ...")
                x=int(input(" 1 ---> Update once more.\n 2 ---> Exit\n \t CHOICE :~ "))
                if x==2 :
                    break 
            if z ==4:
                break
            print("\n","_"*25,"\n\n\t    MAIN MENU    ","\n","_"*25)
    if a == 5:
        while True:
            print('Rooms Type to Book:')
            m=int(input(" 1 ---> AC\n 2 ---> DELUX\n 3 ---> SUPER DELUX\n 4 ---> QUEEN DELIGHT\n 5 ---> KING SPECIAL\n\n Press 6 to EXIT.\n\t\t Choice:__"))
            if m==1:
                print("\n","_"*50,"\n\n\t AVAILABLE AC ROOM  ","\n","_"*50)
                cursor.execute("Select * from rooms where Status = 'FREE' and ROOM_TYPE='AC';")
                data=cursor.fetchall()
                for i in data:
                    if len(i)==0:
                        print("NO Rooms available FREE in this category.")
                    if len(i)!=0:
                        print(" Room no.",i[1],"\n Description :",i[2],"\n Rent: ",i[3],"\n Bed Type: ",i[4],"\n Status :",i[5],"\n\n")
                        print("_"*30)
                        
            if m==2:
                print("\n","_"*50,"\n\n\t AVAILABLE DELUX ROOM  ","\n","_"*50)
                cursor.execute("Select * from rooms where Status = 'FREE' and ROOM_TYPE='DELUX';")
                data=cursor.fetchall()
                for i in data:
                    if len(i)==0:
                        print("NO Rooms available FREE in this category.")
                    if len(i)!=0:
                        print(" Room no.",i[1],"\n Description :",i[2],"\n Rent: ",i[3],"\n Bed Type: ",i[4],"\n Status :",i[5],"\n\n")
                        print("_"*30)
                    
                    
                        
            if m==3:
                print("\n","_"*50,"\n\n\t AVAILABLE SUPER DELUX ROOM  ","\n","_"*50)
                cursor.execute("Select * from rooms where Status = 'FREE' and ROOM_TYPE='SUPER DELUX';")
                data=cursor.fetchall()
                for i in data:
                    if len(i)==0:
                        print("NO Rooms available FREE in this category.")
                        break
                    if len(i)!=0:
                        print(" Room no.",i[1],"\n Description :",i[2],"\n Rent: ",i[3],"\n Bed Type: ",i[4],"\n Status :",i[5],"\n\n") 
                        print("_"*30)
                       
                                 
            if m==4:
                print("\n","_"*50,"\n\n\t AVAILABLE QUEEN DELIGHT ROOM  ","\n","_"*50)
                cursor.execute("Select * from rooms where Status = 'FREE' and ROOM_TYPE='QUEEN DELIGHT';")
                data=cursor.fetchall()
                for i in data:
                    if len(i)==0:
                        print("NO Rooms available FREE in this category.")
                    if len(i)!=0:
                        print(" Room no.",i[1],"\n Description :",i[2],"\n Rent: ",i[3],"\n Bed Type: ",i[4],"\n Status :",i[5],"\n\n")
                        print("_"*30)
                       
            if m==5:
                print("\n","_"*50,"\n\n\t AVAILABLE KING SPECIAL ROOM  ","\n","_"*50)
                cursor.execute("Select * from rooms where Status = 'FREE' and ROOM_TYPE='KING SPECIAL';")
                data=cursor.fetchall()
                for i in data:
                    if len(i)==0:
                        print("NO Rooms available FREE in this category.")
                    if len(i)!=0:
                        print(" Room no.",i[1],"\n Description :",i[2],"\n Rent: ",i[3],"\n Bed Type: ",i[4],"\n Status :",i[5],"\n\n")
                        print("_"*30)
                        
                   
            
            if m==6:
                break
            roomid=int(input("Enter Room no. to book :~"))
            name=input("Customer's name: ")   
            cursor.execute("Select id,name,phone from customer where name like '%{}%';".format(name))
            data1=cursor.fetchall()
            print("\n","_"*50,"\n\n\t   DISPLAYING CUSTOMER DATA TO FIND CUST_ID   ","\n","_"*50)
            for a in data1:
                print(" ID :- ",a[0],"\n Name :-",a[1],"\n Phone no.",a[2])
                print("_"*30)
                print("\n")    
                print("\n")
               
            custid=int(input("Enter customer ID:~ "))
            doo=input("Date Of Occupance (YYYY-MM-DD):~ ")
            dol=input("Date of Leaving (YYYY-MM-DD) :~ ")
            advance=float(input("Enter the Advance amount Paid(in Rs.) : "))
            cursor.execute("insert into booking (ROOM_ID,CUST_ID,DOO,DOL,ADVANCE) Values ({},{},'{}','{}',{});".format(roomid,custid,doo,dol,advance))
            cursor.execute("update rooms set status='OCCUPIED' where room_no = {};".format(roomid))
            cursor.execute("Commit;")
            print("\n","_"*50,"\n\n\t   BOOKING SUCCESSFULLY DONE...   ","\n","_"*50)   
        
        print("\n","_"*25,"\n\n\t    MAIN MENU    ","\n","_"*25)
    if a == 6:
        while True:
            name=input("Customer's name: ")   
            cursor.execute("Select id,name,phone from customer where name like '%{}%';".format(name))
            data1=cursor.fetchall()
            print("\n","_"*50,"\n\n\t   DISPLAYING CUSTOMER DATA TO FIND CUST_ID   ","\n","_"*50)
            for a in data1:
                print(" ID :- ",a[0],"\n Name :-",a[1],"\n Phone no.",a[2])
                print("_"*30)
            print("\n")       
            
            custid=input("\nEnter the customer ID: ")

            print("\n\t","_"*25,"\n\n\t\t   BILL   ","\n\t","_"*25)
            cursor.execute("select now();")
            billdate=cursor.fetchone()[0]
            print(" Date and time of billing :",billdate)
            cursor.execute("Select name from customer where id={};".format(custid))
            aa=cursor.fetchone()
            print("Customer Name: ",aa[0])
            cursor.execute("Select book_id from booking where cust_id={};".format(custid))
            aa=cursor.fetchall()
            for i in aa:
                print("Booking ID: ",i[0])
            cursor.execute("Select phone from customer where id={};".format(custid))
            aa=cursor.fetchall()
            for i in aa:
                print("Phone Number: ",i[0])
            cursor.execute("Select email_id from customer where id={};".format(custid))
            aa=cursor.fetchall()
            for i in aa:
                print("Email ID: ",i[0])
            print("_"*25)
            query1="Select doo from booking where cust_id={};".format(custid)
            query2="Select dol from booking where cust_id={};".format(custid)
            cursor.execute(query1)
            doo=cursor.fetchone()
            cursor.execute(query2)
            dol=cursor.fetchone()
            print("Date of Occupance: ",doo[0])
            print("Date of Checkout: ",dol[0])
            print("_"*25)
            cursor.execute("select dayofyear('{}');".format(doo[0]))
            mn=cursor.fetchone()[0]
            cursor.execute("select dayofyear('{}');".format(dol[0]))
            mno=cursor.fetchone()[0]
            day=mno-mn
            print("No. of days stayed :- ",day)
            cursor.execute("Select value from TAX where tax='gst';")
            gst=cursor.fetchone()[0]
            cursor.execute("Select value from TAX where tax='st';")
            st=cursor.fetchone()[0]
            cursor.execute("Select room_id from booking where cust_id={};".format(custid))
            roomid=cursor.fetchone()
            cursor.execute("Select room_no from rooms where id ={};".format(roomid[0]))
            roomno=cursor.fetchone()[0]
            cursor.execute("Select room_rent from rooms where room_no={};".format(roomno))
            roomrent=cursor.fetchone()[0]
            print("Room Rent :- ",roomrent)
            print("_"*25)
            total=day*roomrent
            print("Total Rent of Stay :-\tRs.",total)
            cursor.execute("Select advance from booking where cust_id={};".format(custid))
            advance=cursor.fetchone()[0]
            print("Advance Amount Paid:-\tRs.",advance)
            print("GST:-\t",gst,"%")
            print("Service Tax (ST):-\t",st,"%")
    
            amount = total-advance
            print("Total Amount (Without gst and st):-\tRs.",amount)
            gstrs=amount*gst/100
            strs=amount*st/100
            cursor.execute("Select book_id from booking where cust_id = {};".format(custid))
            bookid=cursor.fetchone()[0]
            totalreal=amount+gstrs+strs
            cursor.execute("insert into bill (book_id,amount,bill_date,GST,ST) Values ({},{},'{}',{},{});".format(bookid,amount,billdate,gst,st))
            cursor.execute("commit;")
            print("Taxes:\tRs.",gstrs+strs)
            print("Total Amount to be Paid :\t",totalreal)
            input("Payment by (UPI/PhonePe/Net Banking/ Cash):- ")
            print("\n\t PAYMENT DONE SUCCESSFULLY...\n")
            
            print("\n","_"*50,"\n\n\t   THANKS FOR VISITING. VISIT AGAIN.  ","\n","_"*50)   
            cursor.execute("UPDATE rooms set status='FREE' where room_no={};".format(roomno))
            cursor.execute("Commit;")
            
            break
        print("\n","_"*25,"\n\n\t    MAIN MENU    ","\n","_"*25)
            
    if a ==7:
        while True:
            name=input("Customer's name: ")   
            cursor.execute("Select id,name,phone from customer where name like '%{}%';".format(name))
            data1=cursor.fetchall()
            print("\n","_"*50,"\n\n\t   DISPLAYING CUSTOMER DATA TO FIND CUST_ID   ","\n","_"*50)
            for a in data1:
                print(" ID :- ",a[0],"\n Name :-",a[1],"\n Phone no.",a[2])
                print("_"*30)
            custid=input("\nEnter the customer ID:")
            cursor.execute("set foreign_key_checks=0")
            cursor.execute("Delete from customer where id={};".format(custid))
            cursor.execute("set foreign_key_checks=1")
            cursor.execute("Commit;")
            print("\n","_"*50,"\n\n\t   Customer information successfully Removed.   ","\n","_"*50)
            print("\n","_"*25,"\n\n\t    MAIN MENU    ","\n","_"*25)
            print("\n")
            break
    
     
    if a ==8:
        abc=input("Enter the PASSWORD to customize the program:-\t")
        if abc=="mridul@mysql":
            gstst=int(input("1. ---> Change GST.\n2. ---> Change Service Tax (ST)\n\tCHOICE:~"))
            if gstst== 1:
                changegst=float(input("CHANGE GST to __"))
                cursor.execute("Update tax set value={} where TAX = 'gst';".format(changegst))
                cursor.execute("Commit;")
                print("\n","_"*50,"\n\n\t   Successfully CHANGED   ","\n","_"*50)
                print("\n","_"*25,"\n\n\t    MAIN MENU    ","\n","_"*25)
                
            if gstst== 2:
                changest=float(input("CHANGE ST to __"))
                cursor.execute("Update tax set value={} where TAX = 'st';".format(changest))
                cursor.execute("Commit;")
                print("\n","_"*50,"\n\n\t   Successfully CHANGED   ","\n","_"*50)
                print("\n","_"*25,"\n\n\t    MAIN MENU    ","\n","_"*25)
            if gstst>2 or gstst<1:
                print("\n","_"*50,"\n\n\tInvalid Response.","\n","_"*50)
                print("\n","_"*25,"\n\n\t    MAIN MENU    ","\n","_"*25)
                
        else:
             print("\n","_"*50,"\n\n\t  INVALID PASSWORD  ","\n","_"*50)
             print("\n","_"*25,"\n\n\t    MAIN MENU    ","\n","_"*25)
          
        
            
    if a == 9:
        print("\n","_"*50,"\n\n\t   THANKS FOR USING THIS MANAGEMENT SYSTEM   ","\n","_"*50)   
        break
            
        
    
