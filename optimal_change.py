import math

def get_change(cost, paid):
    # Create a map of money to run our change through
    money = {"$100 dollar bill":100,"$50 dollar bill":50, "$20 dollar bill":20, "$10 dollar bill":10, "$5 dollar bill":5, "$1 dollar bill":1, "quarter":.25, "dime":.10, "penny":.01}
    
    # Create a variable to hold our initial subtraction (Round to the nearest 2nd decimal place!)
    change = round((paid - cost), 2)

    # Check to see if any change is returned
    if change == 0:
        return("Perfect Change!")
    # Checking to see if the amount paid was enough to meet the cost
    if change >= 0:
        pass
    else :
        return("Not enough money!")
    
    # Lists to push our amounts
    list_howMany = []
    list_howMuch = []
    
    # Loop through our money map and assign out values to our lists
    for key in money :
        if money[key] <= change :
                amount_of_bills = int(change // money[key])
                change = round((change - money[key] * amount_of_bills), 2)
                list_howMany.append(amount_of_bills)
                list_howMuch.append(money[key])
    
    # Create an empty string that will hold our values in the correct format
    input = " "
    
    # Loop through both of our lists and add them in the correct format to our list
    for howMany, howMuch in zip(list_howMany, list_howMuch):
        if howMuch >= 1: 
            input += f"{howMany} ${howMuch}"
            if howMany > 1:
                input += " bills, "
            else: 
                input += " bill, "
        elif howMuch == .25:
            input += f"{howMany}"
            if howMany > 1:
                input += " quarters, "
            else: 
                input += " quarter, "
        elif howMuch == .10:
            input += f"{howMany}"
            if howMany > 1:
                input += " dimes, "
            else: 
                input += " dime, "
        elif howMuch == .01:
            input += f"and {howMany}"
            if howMany > 1:
                input += " pennies."
            else: 
                input += " penny."
    
    # Assign last variable to hold our final statement, taking in all appropriate variables
    answer = (f"The optimal change for an item that costs ${cost} with an amount paid of ${paid} is{input}")
    
    print(answer.strip(' ,'))
    return(answer.strip(' ,'))
    
# My attempt to factor in the "and" failed. Below are the items I was working with.
# list_of_money = []
# list_of_money.append(f"{howMany} ${howMuch}")
# for x in list_of_money:
    #     Add an "and" in front of the last item in the list
    #     Append all items to a string
# print(list_of_money)