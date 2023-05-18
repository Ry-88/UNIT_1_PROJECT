from Drinks_page import order_list,price_list


dict_dounts = {"Glazed":5, "Blueberry":7, "Glazed Chocolate":6, "Long John":6, "Boston Cream":6}

name_donuts = list(dict_dounts.keys())
price_donuts = list(dict_dounts.values())

def donuts():
    count = 1
    print("\n Donuts")

    for i in range(len(name_donuts)):
        print(f"{count}-{name_donuts[i]} {price_donuts[i]}.SR \n")
        count +=1

def take_order(type:str,order:str):
    if type.lower() == "dn" or type.lower() == "donuts": 
        if order in name_donuts:
            order_list.append(order)
            price_list.append(dict_dounts[order])
            print("added to the invoice")
            return
        else:
            print("please check the name of order")

    else:
        print("Please check the input!")

def print_your_order():
    count = 1
    print("\n You added this items ")
    
    for i in range(len(order_list)):
        print(f"{count}-{order_list[i]} {price_list[i]}.SR \n")
        count +=1