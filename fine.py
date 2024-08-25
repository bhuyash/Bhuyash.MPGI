ch="yes"
while ch.lower()=="yes":


  att=int(input("Enter Students Attendance:"))
  print(f"Your attendence is {att}%")
  if att<0 or att>100:
    print("Please Enter Valid Attendence..")
  elif att<=100 and att>=95:
    print("Congratulations You Might Get a Reward!!")
  elif att<95 and att>=90:
    print("You Don't Have to give any fine")
  elif att<90 and att>=85:
    print("You have to pay the fine--500RS")
  elif att<85 and att>=80:
    print("You have to pay the fine--1000RS")
  elif att<80 and att>=75:
    print("You have to pay the fine--1500RS + You have to do assignment of each subject")
  else:
    print("__You are not eligible for test Please Contact Your Coordinator__")
  ch=input("If you want to check more attendence enter yes: ")