# 1. Your Database
name = {
    "Daniel": {"amount": 10000, "pin": 1111},
    "David": {"amount": 20000, "pin": 1111},
    "Esther": {"amount": 30000, "pin": 1111},
    "Joy": {"amount": 1000, "pin": 1111},
    "Michael": {"amount": 6000, "pin": 1111}
}

# 2. Login
names = input('enter name ').strip().title()

if names in name:
    pin = int(input('enter your pin '))
    
    if pin == name[names]['pin']:
        print('checking...')
        print("-" * 25)
        
        # We ask for the first transaction
        transaction = input("enter 'new' to withdraw or 'exist' to stop: ").lower()
        
        while transaction != 'exist':
            amounts = int(input('enter the amount you want to withdraw '))
            
            # THE FIX: Check balance vs the dictionary
            if amounts <= name[names]['amount']:
                # THE UPDATE: This line changes the memory
                name[names]['amount'] -= amounts
                
                print(f"collect your money below")
                print(f"your remaining balance is {name[names]['amount']}")
            else:
                print(f"Insufficient funds! Your balance is {name[names]['amount']}")
            
            # Ask again to keep the loop going or stop it
            transaction = input("enter 'new' to withdraw more or 'exist' to stop: ").lower()

        print('THANK YOU FOR PATRONIZING US')
    else:
        print('wrong password')
else:
    print('try another name in the dictionary')