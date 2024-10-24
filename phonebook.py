#PHONE -BOOK

user_dict1={}
li=[]
print("click 1 to create your contact")
print("click 2 to view  the information")
print("click 3 to update the contact")
print("click 4 to delete or remove your information")
print("click 5 to print the dictionary")
print("click 6 to exit")

while 1:
    choice=int(input("enter your choice"))

    if(choice==1):
        name=input("enter your name")
        age=int(input("enter your age"))
        email=input("enter your email")
        phone_no=int(input("enter your phone number"))
        li.append(age)
        li.append(email)
        li.append(phone_no)
        user_dict1[name]=li

    elif(choice==2):
       namecollector=input("enter the name whose information you need ")
       print(user_dict1[namecollector])

    elif(choice==3):
        changer=input("enter whose value you want to update(age,email,phone_no)")
        if(changer=="age"):
            newage=int(input("enter your new age"))
            user_dict1[name][0]=newage  
        elif(changer=="email"):
           newemail=input("enter your new email")
           user_dict1[name][1]=newemail
        elif(changer==phone_no):
           newphone_no=int(input("enter your new phone number"))
           user_dict1[name][2]=newphone_no
        else:
           print("invalid input")
    elif(choice==4):
         delete=input("enter the name your information you want to remove")
         del user_dict1[name]
    elif(choice==5):
        print(user_dict1)
    elif(choice==6):
        break
    else:
         print("invalid choice")

     
