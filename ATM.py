print("\t\t\t\t\t ATM Machine \t\t\t\t\t")
pin=4321
global balance
balance=10000
def Withdraw():
  global balance
  x=int(input("How much amount you want to withdraw: "))
  if x>balance:
    print("insufficient funds!!")
  else:
    balance=balance-x
    print(f"You withdrew RS{x}")
    print(f"Now your balance is:{balance}")
def check():
  print("Your current account balance is",balance)
def Deposit():
  global balance
  y=int(input("How much amount you want to Deposit: "))
  balance=balance+y
  print(f"You Deposited RS{y}")
  print(f"Now your balance is:{balance}")
  
while True:
  p=int(input("Enter Your PIN to Start any operation: "))
  if(p==pin):
    print("Enter 1 to check the Account Balance: ")
    print("Enter 2 to Withdraw from the Account: ")
    print("Enter 3 to Deposit an Amount into the account: ")
    ch=int(input("which Operation do you want to perform: "))
    if(ch==1):
      check()
    elif(ch==2):
      Withdraw()
    elif(ch==3):
      Deposit()
    else:
      print("Enter A Right Choice\n Enter 1,2 or 3 please!!")
  else:
    print("Incorrect pin")
  c=(input("Enter yes to perform more operation or enter exit to Exit: "))


  