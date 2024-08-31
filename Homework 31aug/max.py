a=int(input("Enter how many numbers you want to Input:"))
i=1
m=0
while(i<=a):
  n=int(input(f"Enter the {i} Number:"))
  if(n>m):
    m=n
  i+=1
print("The maximum number you entered is:",m)

  