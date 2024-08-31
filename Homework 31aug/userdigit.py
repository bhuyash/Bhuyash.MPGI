dig=int(input("Enter the number of digits you want:"))
i=1
s=0
while(i<=dig):
  n=int(input(f"Enter the {i} digit of a number: "))
  if(n<0):
    print("please enter a positve number!!!")
  else:
   s=s+n
   i+=1

print("The sum of Digits of a number you entered is:",s)