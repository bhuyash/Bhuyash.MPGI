num=int(input("Enter the number"))
a=num
sum=0
if(num<0):
  print("Negative sign will be ignored")
  a=num*(-1)
while(a>0):
  rem=a%10
  sum=sum+rem
  a=a//10
print(f"The digit sum of {num} is {sum}")