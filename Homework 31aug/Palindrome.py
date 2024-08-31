num=int(input("Enter the number"))
a=num
rev=0
if(num<0):
  print("Negative number can never be palindromic")
else:
  while(a>0):
    rem=a%10
    rev=rev*10+rem
    a=a//10
  if(num==rev):
    print(f"The number: {num} is a palindrome number")
  else:
    print(f"Number: {num} is not palindromic")