num=int(input("Enter a decimal number:"))
a=num
binn=""
while(num>0):
  rem=num%2
  binn=str(rem)+binn
  num=num//2
print(f"Decimal Value:{a}\nBinary Vale: {binn}")

