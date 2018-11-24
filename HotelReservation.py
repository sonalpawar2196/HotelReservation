import os
import csv

print " Hotel Reservation System "







userList = [{"password":"Sonal","Contact_No":32543545,"Email":"sonal@gmail.com"},{"password":"Priya","Contact_No":45354535,"Email":"priya@gmail.com"},{"password":"mona","Contact_No":32543545,"Email":"mona@gmail.com"}]
HotelList = [{"Hotel_Name":"President","Room":[1,2,3,4,5]},{"Hotel_Name":"Palash","Room":[1,2,3,4,5]},{"Hotel_Name":"prithvi","Room":[1,2,3,4,5]},]

row = ['t@gmail.com', ' 32545324', 'T']



'''
with open('Users.csv','w') as file :
    fields = ['Email','password','Contact_No']
    writer = csv.DictWriter(file,fieldnames = fields)
    writer.writeheader()
    writer.writerows(userList)

with open('Users.csv', 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(row)
 '''

with open('Users.csv','r') as file:
    reader = csv.reader(file)
    for row in reader:
        print row
'''
with open('Hotels.csv','w') as file :
    fields = ['Hotel_Name','Room']
    writer = csv.DictWriter(file,fieldnames = fields)
    writer.writeheader()
    writer.writerows(HotelList)
'''   
with open('Hotels.csv','r') as file:
    reader = csv.reader(file)
    for row in reader:
        print row

    

def Login():
    name = raw_input("Enter Email : ")
    password = raw_input("Enter password : ")
    flag = 0
    with open('Users.csv','r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == name and row[1] == password:
                flag = 1
                break
            else:
                flag = 0
        if flag == 1:
                print "Logged In"
        else:
                print "Invalid"

        return name
            
                
                
def Booking():
    Booking.name = raw_input("Enter hotel Name : ")
    Booking.room_No = int(input("select room number: "))

    with open('Hotels.csv','r') as file:
        reader = csv.reader(file)
        count = 0
        count1 = 0
        for j in reader:
            if j[0]==Booking.name:
                count = count + 1
                print "Hotel available"
                for i in j[1]:
                    if i!="," or i!="[" or i!="]" and i==Booking.room_No:
                        count1 += 1
                        print "Room  "+str(Booking.room_No)+" Selected"
                        break
                    
        if count < 1:
                print "Hotel not available"
        if count1 < 1:
                print "Room not available"
        
        print "logged in user : ",logged_in_user
        
        with open('Users.csv','rw') as file:
            reader = csv.reader(file)
            for k in reader:
                if k[0]==logged_in_user :
                    k.append("Hotel")
                    for item in reader:
                        item.append(Booking.name)
                  


def cancelation():
    room_no = Booking.room_No
    hotel_name = Booking.name
    confirm = raw_input("Do you want to cancel Booking Y/N : ")
    if str(confirm) == "Y":
        for k in userList:
            if k["Email"]==logged_in_user :
                k.pop ("Hotel")
                #k.pop["Room_No"]
                print userList
            else:
                print hotel_name,room_no
                print "booking cancelled"
            
    

print userList
logged_in_user = Login()
print logged_in_user
Booking()
cancelation()
    





