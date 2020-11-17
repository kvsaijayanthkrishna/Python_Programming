total_accounts={101:50000,102:45000,103:55000}
print("current accounts present",total_accounts,sep="\n")
Id=int(input("Enter Account ID:"))
amt=int(input("Enter Amount:"))
new_account={Id:amt}
balance=total_accounts.get(Id)
total_accounts.update(new_account)
if balance != None:
    print("Account updated")
    total_accounts[Id]=balance+amt
else : print("New Account created")
print("Account Details",total_accounts,sep="\n")

