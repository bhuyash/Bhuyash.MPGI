import random
m="yes"
li=[]
while(m=="yes"):
  st="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLMNBVCXZ`1234567890-=+!@#$%^&*"
  l=int(input("Enter length of password:"))
  if l<1:
      print("please enter valid value")
      continue
  pas=""
  for _ in range(l):
     r=random.choice(st)
     pas=pas+r
  print("your random password is:",pas)
  li.append(pas)
  print(li)
  c=li.count(pas)
  if c>1:
      print("password is repeated")
  else:
      print("Password is not repeating")
  m=input("enter yes if you want to generate other password:")
