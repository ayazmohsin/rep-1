usd = 3.67
euro = 3.97
gbp = 4.65


def aed_to_other(usr_aed , x):
    if x == 1:
        print (usr_aed % usd)
    elif x == 2:
        print (usr_aed % gbp)
    elif x == 3:
        print (usr_aed % euro)
    else:
        print ("Incorrect selection! ")

def other_to_aed(curr_type , amount):
    if curr_type == 1:
        print (amount * usd)
    elif curr_type == 2:
        print (amount * gbp)
    elif curr_type == 3:
        print (amount * euro)
    else:
        print ("Incorrect selection! ")

def main():
    service = input(" Type \"1\" to convert from AED to other currencies \n Type \"2\" to convert from Other currencies to AED ")
    if service == 1:
        user_aed = int(input("Please type the amount of money you want to convert"))
        x = ("1 to convert to USD \n 2 to convert to GBP \n 3 to convert to Euro")
        aed_to_other(x)
    elif service == 2:
        amount = ("How much currency do you want to convert?")
        curr_type = input("what currency would you like to convert from? \n 1 for USD \n 2 for GBP \n 3 for Euro")
        other_to_aed(curr_type)
    else:
        break

main()
    



