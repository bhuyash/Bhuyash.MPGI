#PHONE -BOOK

phone={}
print("click 1 to create your contact")
print("click 2 to view  the information")
print("click 3 to update the contact")
print("click 4 to delete or remove your information")
print("click 5 to show whole phonebook")
print("click 6 to exit")

while 1:
    choice=int(input("enter your choice:"))

    if(choice==1):
        name=input("enter your name:")
        age=int(input("enter your age:"))
        email=input("enter your email:")
        phone_no=int(input("enter your phone number:"))
        phone[name]={"Name":name,"Age":age,"Email":email,"Phone No":phone_no}

    elif(choice==2):
       n=input("enter the name whose information you need: ")
       print(phone[n])

    elif(choice==3):
        n=input("Which contacts details you want to update:")
        changer=input("enter whose value you want to update(age,email,phone_no):")
        if(changer=="age"):
            newage=int(input("enter your new age:"))
            phone[n]["Age"]=newage  
        elif(changer=="email"):
           newemail=input("enter your new email:")
           phone[n]["Email"]=newemail
        elif(changer==phone_no):
           newphone_no=int(input("enter your new phone number:"))
           phone[n]["Phone_no"]=newphone_no
        else:
           print("invalid input")
    elif(choice==4):
         delete=input("enter the name whose information you want to remove:")
         del phone[delete]
    elif(choice==5):
        print(phone)
    elif(choice==6):
        break
    else:
         print("invalid choice")
