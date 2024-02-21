age = 12


if age == 12:
    print('you are ready')
else :
    print('you are not ready')




 #---------------------- if confdition for lsit ---------------

Garage = ['Toyota','Lexus', 'Tesla', 'BMW', 'Volvo']

Car = 'Neta'

if Car in Garage:
    print(f"There is {Car} in your garage")
else:
    print(f'there is no {Car} in your Garage. Do you want to buy one?')



 #---------------------- if confdition for Dictionary ---------------
Mobile = {'fluketoon':'0831333229', 'My Mom':'0863450835', 'My Babe':'0894433795'}
MobileNumber = Mobile.values()

def FindMyNumber(Name):
    if Name in Mobile:
        print(Mobile[Name])
    else:
        print(f'there is no {Name} in your contact')

FindMyNumber('My Mom')
FindMyNumber('fluketoon')
FindMyNumber('ahora')


# def FindMyName(PhoneNumber):
#     if PhoneNumber in MobileNumber:
#         print(Mobile.keys())
#         print(Mobile.values())
#     else:
#         print(f'there is no {PhoneNumber} in your contact')

# FindMyName('0831333229')


 #---------------------- if confdition for List ---------------

StyleList = ["Thailand", "Japan", "USA", "UK"]

def CheckStyle(Style, Money):
    if Money>= 1000 and Style in StyleList:
        print("you are allowed to come in")
    elif Style not in StyleList and Money > 2000:
        print("you are not in the list but you have enogh money. You can come in!!")
    else:
        print("you are not allowed to come in")

CheckStyle("Japan",10000)
CheckStyle("USA",500)
CheckStyle("Vietnam",5000)
CheckStyle("Thailand", 100)
    
