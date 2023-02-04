import mysql.connector as my
import datetime
import pywhatkit
#speaker=pyttsx3.init()

#def speak(text):
####   speaker.say(text)
#   speaker.runAndWait()
   


l1=open("password.txt",'w')    
a=input("SET USERNAME")
b=input("SET PASSWORD")
print()
print("Username And Password Sucessfully Set")
d=""
l3=open("username.txt",'w')   ## saving the username in file
l3.write(a)
l3.close()

l31=open("username.txt",'r')   ## saving the password in file
l=l31.read()
l31.close()


 #this is used for encrption
 #password cant be read through text file manually
for i in b:     
   s=ord(i)     
   s=s+1
   i=chr(s)
   d=d+i      #the 2nd alphabet to the respective alphabet is saved in the word file
b=d
    
l1.write(b)
l1.close()


l2=open("password.txt",'r')
s=l2.read()
j=""
for i in s:
    k=ord(i)
    k=k-1
    i=chr(k)
    j=j+i
s=j
l2.close()
print()


x1=input("Enter Username")
y1=input("Enter Password")
print()



# if the password is correct
if x1==l and y1==s:
  #  speak("welcome sir")
    u=input("Do You Want To Reset Username And Password (yes/no)")
    if u.lower()=="yes":
             u1=input("Enter New Username")
             u2=input("Enter New Password")
             l3=open("username.txt",'w')
             l3.write(u1)
             l3.close()
             b=""

             for i in u2:
                 s=ord(i)
                 s=s+1
                 i=chr(s)
                 d=d+i
                 b=d
                 l1=open("password.txt",'w')
                 l1.write(b)
                 l1.close()

             print("USERNAME AND PASSWORD SUCESSFULLY RESET")
      
             print()
            
                 
    elif u.lower()=="no":   
         print()

    else:
         print("Invalid Choice")
         print()


    n=1
    while n==1:
        # connecting to mysql
       mydb=my.connect(host="localhost",user="root",passwd="",database="drugstore")
       mycursor=mydb.cursor()
       a=int(input(("Table you want to use\n1)CUSTOMER\n2)SALES\n3)MEDICINES\n4)COMPOSITION OF ANY MEDICINE\n5)EXIT")))
       print()

#Using CUSTOMER table
       if a==1:
           #the first tables option
           mycursor.execute("select count(*) from customer")
           for i in mycursor:
               print("No Of Records In Customer Is",i)
               print()
               #the no of pre existing records in the table
           
           a1=int(input("1)ADD\n2)SEARCH\n3)DELETE\n4)FULL RECORD"))
           if a1==1:
               a11=input("Enter Customer Name")
               a12=datetime.date.today()  # taday's date is set automatically
               a13=input("Medicine Sold")
               a14=input("QTY")
               mycursor.execute("INSERT INTO customer(CName,Date,medicine_sold,QTY)VALUES('{}','{}','{}',{})".format(a11,a12,a13,a14))
               mydb.commit()
               print()
               print("ADDED SUCCESSFULLY")
               print()

            #searching in the table
           elif a1==2:
               a30=int(input("1)Search On Basis Of Name\n2)Search On Basis Of Date"))
               if a30==1:
                   a31=input("Enter Name To Searched")
                   mycursor.execute("select * from customer where CName=%s",(a31,))
                   print("Name\t\tDate\t\tMedicine\t\tQuantity")
                   for i in mycursor:
                       print(i[0],'\t\t',i[1],'\t',i[2],'\t\t',i[3])
                       print()

               elif a30==2:
                   a32=input("Enter Date")
                   mycursor.execute("select * from customer where Date=%s",(a32,))
                   print("Name\t\tDate\t\tMedicine\t\tQuantity")
                   for i in mycursor:
                       print(i[0],'\t\t',i[1],'\t',i[2],'\t\t',i[3])
                       print()

            #deleting record from tables

           elif a1==3:
               a41=input("Enter Name To Be Deleted")
               mycursor.execute("delete from customer where CName=%s",(a41,))
               mydb.commit()
               print("Deleted Sucessfully")
               print()

           # the full record is shown according to recent addition in the table

           elif a1==4:
               mycursor.execute("select * from customer order by Date desc")
               print()
               print("Name\t\tDate\t\tMedicine\t\tQuantity")
               
               
               for i in mycursor:
                   print(i[0],'\t\t',i[1],'\t',i[2],'\t\t',i[3])
                   print()
#Using SALES table           
       elif a==2:
           b1=int(input("Enter Your Choice \n1)ADD \n2)VIEW \n3)UPDATE"))
           print()
           if b1==1:
               
               b12=input("Enter Company Name")
               b13=input("Medicine Imported")
               b14=input("Date Of Import")
               b15=input("Date Of Payment")
               b16=int(input("Payment Amount"))
          #inserting into the table     
               mycursor.execute("INSERT INTO company(company_name,medicines_imported,Date_OF_Import,Date_OF_Payment,Payment_Amount)VALUES('{}','{}','{}','{}',{})".format(b12,b13,b14,b15,b16))
               mydb.commit()
               print()
               print("ADDED SUCCESSFULLY")
               print()

                # the company records are added to the sales table automatically
               mycursor.execute("INSERT INTO sales(company_name)VALUES('{}')".format(b12))
               mydb.commit()
               print()

          # showing all the comany records
           elif b1==2:
               mycursor.execute("select * from sales")
               print("Company Name")
               for i in mycursor:
                   print(i)
               print()

               #showing the detalied info of the company
               b21=input("Enter Company Name To View It's Details")
               
               mycursor.execute("select * from company where company_name=%s",(b21,))
               print("No.\t\tName\t\tMedicine\t\tDate of import\t\tDate of Payment\t\tAmount")
               for i in mycursor:
                   print(i[0],'\t\t',i[1],'\t',i[2],'\t\t',i[3],'\t\t',i[4],'\t\t',i[5])
                   print()

           elif b1==3:
              mycursor.execute("select * from company")
              for i in mycursor:
                 print(i) 

            # updating the records 
              b31=int(input("Enter Company No. You Want To Udpdate"))
              mycursor.execute("select * from company where cno=%s",(b31,))
              for i in mycursor:
                 print(i)
                 print()
              b37=int(input("What Do You Want To Change:\n1)COMPANY NAME\n2)MEDICINE IMPORTED\n3)DATE OF IMPORT\n4)DATE OF PAYMENT\n5)PAYMENT AMOUNT"))
              print()
              if b37==1:
                    b32=input("Enter Upadated Company Name")
                    mycursor.execute("UPDATE company set company_name=%s where cno=%s",(b32,b31))
                    mycursor.execute("UPDATE sales set company_name=%s where cno=%s",(b32,b31))
                    
                    mydb.commit()

              elif b37==2:
                   b33=input("Enter Upadated Imported Medicine Name")
                   mycursor.execute("UPDATE company set medicines_imported=%s where cno=%s",(b33,b31))
                   mydb.commit()
                   print()

              elif b37==3:
                   b34=input("Enter Upadated Date Of Import")
                   mycursor.execute("UPDATE company set Date_OF_Import=%s where cno=%s",(b34,b31))
                   mydb.commit()
                   print()


              elif b37==4:
                   b35=input("Enter Upadated Date Of Payment")
                   mycursor.execute("UPDATE company set Date_OF_Payment=%s where cno=%s",(b35,b31))
                   mydb.commit()
                   print()

              elif b37==5:
                   b36=input("Enter Upadated Payment Amount")
                   mycursor.execute("UPDATE company set Payment_Amount=%s where cno=%s",(b36,b31))
                   mydb.commit()
                   print()

              else:
                 print("Invalid Choice")
                 print()
#Using MEDICINES table
       elif a==3:
          c1=int(input("Enter Choice\n1)ADD\n2)SEARCH\n3)UPDATE\n4)DELETE\n5)FULL INFO OF MEDICINE"))
          print()
          #inserting into the table
          if c1==1:
             d11=input("Enter Medicine's Name")
             d12=input("Batch no.")
             d13=input("MFD")
             d14=input("EXP")
             d15=int(input("Price"))
             d16=input("Imported By")
             d17=(str(datetime.date.today()))
             d18=d17[:4]+'/'+d17[5:7]+'/'+d17[8:10]  #converting the dae into user given format
             
             #the record can only be added if it has not expired
             if str(d14)>(d18):
                 mycursor.execute("INSERT INTO medicines(medicine,batch_no,mfd,exp,price,imported_by)VALUES('{}','{}','{}','{}',{},'{}')".format(d11,d12,d13,d14,d15,d16))
                 mydb.commit()
                 print()
                 print("SUCESSFULLY ADDED")
                 print()

             else:
                 print("Record cant be added as the medicine has already expired")

                 print()
                 
          elif c1==2:
             c21=input("Enter Medicine To Be Searched")
             mycursor.execute("SELECT * FROM medicines where Medicine=%s",(c21,))
             print("Name\t\tBatch no\t\tMFD\t\tEXP\t\tPrice\t\tImported by")
             d17=(str(datetime.date.today()))
             d18=d17[:4]+'/'+d17[5:7]+'/'+d17[8:10]
             for i in mycursor:
                print(i[0],'\t\t',i[1],'\t\t',i[2],'\t\t',i[3],'\t',i[4],'\t\t',i[5])
                print()
                if str(i[3])<str(d17): # checking the expiry date of medicine
                    print("The Medicine has expired")
                    print()
                else:
                    print()

         #the other record cant be altered coz they r fixed

          elif c1==3:
             print("You Can Only Update Imported By  And Price Column")
             print()
             c30=input("Enter Medicine Name To Update Table ")
             c31=int(input("What Do You Want To Update\n1)Price\n2)Imported by"))
             print()
             if c31==1:
                 c311=int(input("Enter Price"))
                 mycursor.execute("UPDATE  medicines SET price=%s where medicine=%s",(c311,c30))
                 mydb.commit()
                 print("updated sucessfully")
                 print()
             elif c31==2:
                 c32=input("Enter Importer Name")
                 mycursor.execute("UPDATE medicines SET imported_by=%s where medicine=%s",(c32,c30)) 
                 mydb.commit()
                 print("updated sucessfully")
                 print()
             else:
                 print("InValid Choice")

         # deleting from table
          elif c1==4:
              c40=input("Name of medicine you want to delete ")
              mycursor.execute ("DELETE FROM medicines WHERE medicine=%s",(c40,))
              mydb.commit()
              print("Deleted Sucessfully")
              print()
          #showing all records 
          elif c1==5:
              mycursor.execute("SELECT * FROM medicines")
              print("Name\t\tBatch no\t\tMFD\t\tEXP\t\tPrice\t\tImported by")
              for i in mycursor:
                  print(i[0],'\t\t',i[1],'\t\t',i[2],'\t\t',i[3],'\t',i[4],'\t\t',i[5])
                  print()




       elif a==4:
          med=input("enter medicine name to see composition")
          srch="ingrediants of " + str(med)
          pywhatkit.search(srch)
#Quiting the program
       elif a==5:
          n=2

       else:
          print("Invalid Choice")