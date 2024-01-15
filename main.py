milktea = [
    "Cookies & Cream",
    "Cheesecake",
    "Taro"
]
icecoffee = [
    "Macchiato",
    "Moca",
    "Vanilla"
]
total_price = 0
milktea_flavor_name = []
icecoffee_flavor_name = []

admin_username = "chris123"
admin_password = "ryan123"

while True:
    username = input("Enter Admin Username: ")
    password = input("Enter Admin Password: ")
    if username.casefold() == admin_username and password.casefold() == admin_password:
        print("\n\n--------- Successfully Login ---------\n\n")
        print("----------- Welcome to Sip n Sip Tea ----------- \n\n")
        break
    elif username.casefold() != admin_username and password.casefold() == admin_password:
        print("incorrect Username")
    elif username.casefold() == admin_username and password.casefold() != admin_password:
        print("incorrect Password")
    elif username.casefold() != admin_username and password.casefold() != admin_password:
        print("incorrect Username and Password")
    else:
        print("Account not found")

while True:
    menu = input("----------- Menu ----------\nCode    Name \n[1]Milk Tea \n[2]Ice Coffee \nEnter Code =")
    if menu == "1":
        milktea_flavor = input(
            "\nMilk Tea Flavor  \nCode    Name \n[1]" + milktea[0] + "\n[2]" + milktea[1] + "\n[3]" + milktea[
                2] + "\nEnter Code =")
        if milktea_flavor == "1":
            size = input(
                "\n\n----Size and price----\nCode    Name  \n[1]Medium 16oz ₱39 \n[2]Large 22oz ₱49 \nEnter Code =")
            if size == "1":
                quantity = int(input("\nHow many would you like to order?\n="))
                if quantity < 0:
                    print("\nWrong input\n")
                else:
                    add_order = input("\nWould you like to order again?(yes or no)\n=")
                    if add_order.casefold() == "yes":
                        milktea_flavor_name.append(milktea[0])
                        milktea_flavor_name.append("Quantity           :" + str(quantity))
                        milktea_flavor_name.append("Size 16oz          ₱ 39.0\n")
                        price = quantity * 39
                        total_price += price

                    elif add_order.casefold() == "no":
                        milktea_flavor_name.append(milktea[0])
                        milktea_flavor_name.append("Quantity           :" + str(quantity))
                        milktea_flavor_name.append("Size 16oz          ₱ 39.0\n")
                        price = quantity * 39
                        total_price += price
                        break
                    else:
                        print("\nWrong input\n")
            elif size == "2":
                quantity = int(input("\nHow many would you like to order?\n="))
                if quantity < 0:
                    print("\nWrong input\n")
                else:
                    add_order = input("\nWould you like to order again?(yes or no)\n=")
                    if add_order.casefold() == "yes":
                        milktea_flavor_name.append(milktea[0])
                        milktea_flavor_name.append("Quantity           :" + str(quantity))
                        milktea_flavor_name.append("Size 22oz          ₱ 49.0\n")
                        price = quantity * 49
                        total_price += price

                    elif add_order.casefold() == "no":
                        milktea_flavor_name.append(milktea[0])
                        milktea_flavor_name.append("Quantity           :" + str(quantity))
                        milktea_flavor_name.append("Size 22oz          ₱ 49.0\n")
                        price = quantity * 49
                        total_price += price
                        break
                    else:
                        print("\nWrong input\n")
            else:
                print("\nWrong input\n")
        elif milktea_flavor == "2":
            size = input(
                "\n\n----Size and price----\nCode    Name  \n[1]Medium 16oz ₱39 \n[2]Large 22oz ₱49 \nEnter Code =")
            if size == "1":
                quantity = int(input("\nHow many would you like to order?\n="))
                if quantity < 0:
                    print("\nWrong input\n")
                else:
                    add_order = input("\nWould you like to order again?(yes or no)\n=")
                    if add_order.casefold() == "yes":
                        milktea_flavor_name.append(milktea[1])
                        milktea_flavor_name.append("Quantity           :" + str(quantity))
                        milktea_flavor_name.append("Size 16oz          ₱ 39.0\n")
                        price = quantity * 39
                        total_price += price

                    elif add_order.casefold() == "no":
                        milktea_flavor_name.append(milktea[1])
                        milktea_flavor_name.append("Quantity           :" + str(quantity))
                        milktea_flavor_name.append("Size 16oz          ₱ 39.0\n")
                        price = quantity * 39
                        total_price += price
                        break
            elif size == "2":
                quantity = int(input("\nHow many would you like to order?\n="))
                if quantity < 0:
                    print("\nWrong input\n")
                else:
                    add_order = input("\nWould you like to order again?(yes or no)\n=")
                    if add_order.casefold() == "yes":
                        milktea_flavor_name.append(milktea[1])
                        milktea_flavor_name.append("Quantity           :" + str(quantity))
                        milktea_flavor_name.append("Size 22oz          ₱ 49.0\n")
                        price = quantity * 49
                        total_price += price
                    elif add_order.casefold() == "no":
                        milktea_flavor_name.append(milktea[1])
                        milktea_flavor_name.append("Quantity           :" + str(quantity))
                        milktea_flavor_name.append("Size 22oz          ₱ 49.0\n")
                        price = quantity * 49
                        total_price += price
                        break
            else:
                print("\nWrong input\n")
        elif milktea_flavor == "3":
            size = input(
                "\n\n----Size and price----\nCode    Name  \n[1]Medium 16oz ₱39 \n[2]Large 22oz ₱49 \nEnter Code =")
            if size == "1":
                quantity = int(input("\nHow many would you like to order?\n="))
                if quantity < 0:
                    print("\nWrong input\n")
                else:
                    add_order = input("\nWould you like to order again?(yes or no)\n=")
                    if add_order.casefold() == "yes":
                        milktea_flavor_name.append(milktea[2])
                        milktea_flavor_name.append("Quantity           :" + str(quantity))
                        milktea_flavor_name.append("Size 16oz          ₱ 39.0\n")
                        price = quantity * 39
                        total_price += price
                    elif add_order.casefold() == "no":
                        milktea_flavor_name.append(milktea[2])
                        milktea_flavor_name.append("Quantity           :" + str(quantity))
                        milktea_flavor_name.append("Size 16oz          ₱ 39.0\n")
                        price = quantity * 39
                        total_price += price
                        break
                    else:
                        print("\nWrong input\n")
            elif size == "2":
                quantity = int(input("\nHow many would you like to order?\n="))
                if quantity < 0:
                    print("\nWrong input\n")
                else:
                    add_order = input("\nWould you like to order again?(yes or no)\n=")
                    if add_order.casefold() == "yes":
                        milktea_flavor_name.append(milktea[2])
                        milktea_flavor_name.append("Quantity           :" + str(quantity))
                        milktea_flavor_name.append("Size 22oz          ₱ 49.0\n")
                        price = quantity * 49
                        total_price += price
                    elif add_order.casefold() == "no":
                        milktea_flavor_name.append(milktea[2])
                        milktea_flavor_name.append("Quantity           " + str(quantity))
                        milktea_flavor_name.append("Size 22oz          ₱ 49.0\n")
                        price = quantity * 49
                        total_price += price
                        break
                    else:
                        print("\nWrong input\n")
            else:
                print("\nWrong input\n")
        else:
            print("\nWrong Input\n")
    elif menu == "2":
        icecoffee_flavor = input(
            "Ice Coffee Flavor\nCode    Name " + "\n[1]" + icecoffee[0] + "\n[2]" + icecoffee[1] + "\n[3]" + icecoffee[
                2] + "\nEnter Code =")
        if icecoffee_flavor == "1":
            size = input(
                "\n\n----Size and price----\nCode    Name  \n[1]Medium 16oz ₱39 \n[2]Large 22oz ₱49 \nEnter Code =")
            if size == "1":
                quantity = int(input("\nHow many would you like to order?\n="))
                if quantity < 0:
                    print("\nWrong input\n")
                else:
                    add_order = input("\nWould you like to order again?(yes or no)\n=")
                    if add_order.casefold() == "yes":
                        icecoffee_flavor_name.append(icecoffee[0])
                        icecoffee_flavor_name.append("Quantity           :" + str(quantity))
                        icecoffee_flavor_name.append("Size 16oz          ₱ 39.0\n")
                        price = quantity * 39
                        total_price += price
                    elif add_order.casefold() == "no":
                        icecoffee_flavor_name.append(icecoffee[0])
                        icecoffee_flavor_name.append("Quantity           :" + str(quantity))
                        icecoffee_flavor_name.append("Size 16oz          ₱ 39.0\n")
                        price = quantity * 39
                        total_price += price
                        break
                    else:
                        print("\nWrong input\n")
            elif size == "2":
                quantity = int(input("\nHow many would you like to order?\n="))
                if quantity < 0:
                    print("\nWrong input\n")
                else:
                    add_order = input("\nWould you like to order again?(yes or no)\n=")
                    if add_order.casefold() == "yes":
                        icecoffee_flavor_name.append(icecoffee[0])
                        icecoffee_flavor_name.append("Quantity           :" + str(quantity))
                        icecoffee_flavor_name.append("Size 22oz          ₱ 49.0\n")
                        price = quantity * 49
                        total_price += price
                    elif add_order.casefold() == "no":
                        icecoffee_flavor_name.append(icecoffee[0])
                        icecoffee_flavor_name.append("Quantity           :" + str(quantity))
                        icecoffee_flavor_name.append("Size 22oz          ₱ 49.0\n")
                        price = quantity * 49
                        total_price += price
                        break
                    else:
                        print("\nWrong input\n")
            else:
                print("\nWrong input\n")
        elif icecoffee_flavor == "2":
            size = input(
                "\n\n----Size and price----\nCode    Name  \n[1]Medium 16oz ₱39 \n[2]Large 22oz ₱49 \nEnter Code =")
            if size == "1":
                quantity = int(input("\nHow many would you like to order?\n="))
                if quantity < 0:
                    print("\nWrong input\n")
                else:
                    add_order = input("\nWould you like to order again?(yes or no)\n=")
                    if add_order.casefold() == "yes":
                        icecoffee_flavor_name.append(icecoffee[1])
                        icecoffee_flavor_name.append("Quantity           :" + str(quantity))
                        icecoffee_flavor_name.append("Size 16oz          ₱ 39.0\n")
                        price = quantity * 39
                        total_price += price
                    elif add_order.casefold() == "no":
                        icecoffee_flavor_name.append(icecoffee[1])
                        icecoffee_flavor_name.append("Quantity           :" + str(quantity))
                        icecoffee_flavor_name.append("Size 16oz          ₱ 39.0\n")
                        price = quantity * 39
                        total_price += price
                        break
                    else:
                        print("\nWrong input\n")
            elif size == "2":
                quantity = int(input("\nHow many would you like to order?\n="))
                if quantity < 0:
                    print("\nWrong input\n")
                else:
                    add_order = input("\nWould you like to order again?(yes or no)\n=")
                    if add_order.casefold() == "yes":
                        icecoffee_flavor_name.append(icecoffee[1])
                        icecoffee_flavor_name.append("Quantity           :" + str(quantity))
                        icecoffee_flavor_name.append("Size 22oz          ₱ 49.0\n")
                        price = quantity * 49
                        total_price += price
                    elif add_order.casefold() == "no":
                        icecoffee_flavor_name.append(icecoffee[1])
                        icecoffee_flavor_name.append("Quantity           :" + str(quantity))
                        icecoffee_flavor_name.append("Size 22oz          ₱ 49.0\n")
                        price = quantity * 49
                        total_price += price
                        break
                    else:
                        print("\nWrong input\n")
            else:
                print("\nWrong input\n")
        elif icecoffee_flavor == "3":
            size = input(
                "\n\n----Size and price----\nCode    Name  \n[1]Medium 16oz ₱39 \n[2]Large 22oz ₱49 \nEnter Code =")
            if size == "1":
                quantity = int(input("\nHow many would you like to order?\n="))
                if quantity < 0:
                    print("\nWrong input\n")
                else:
                    add_order = input("\nWould you like to order again?(yes or no)\n=")
                    if add_order.casefold() == "yes":
                        icecoffee_flavor_name.append(icecoffee[2])
                        icecoffee_flavor_name.append("Quantity           :" + str(quantity))
                        icecoffee_flavor_name.append("Size 16oz          ₱ 39.0\n")
                        price = quantity * 39
                        total_price += price
                    elif add_order.casefold() == "no":
                        icecoffee_flavor_name.append(icecoffee[2])
                        icecoffee_flavor_name.append("Quantity           :" + str(quantity))
                        icecoffee_flavor_name.append("Size 16oz          ₱ 39.0\n")
                        price = quantity * 39
                        total_price += price
                        break
                    else:
                        print("\nWrong input\n")
            elif size == "2":
                quantity = int(input("\nHow many would you like to order?\n="))
                if quantity < 0:
                    print("\nWrong input\n")
                else:
                    add_order = input("\nWould you like to order again?(yes or no)\n=")
                    if add_order.casefold() == "yes":
                        icecoffee_flavor_name.append(icecoffee[2])
                        icecoffee_flavor_name.append("Quantity           :" + str(quantity))
                        icecoffee_flavor_name.append("Size 22oz          ₱ 39.0\n")
                        price = quantity * 49
                        total_price += price
                    elif add_order.casefold() == "no":
                        icecoffee_flavor_name.append(icecoffee[2])
                        icecoffee_flavor_name.append("Quantity           :" + str(quantity))
                        icecoffee_flavor_name.append("Size 22oz          ₱ 49.0\n")
                        price = quantity * 49
                        total_price += price
                        break
                    else:
                        print("\nWrong input\n")
            else:
                print("\nWrong input\n")
        else:
            print("\nWrong Input\n")
    else:
        print("\nWrong Input\n")

print("\n\n-----Your Order-----\n")
print("Milk Tea Flavor")
for i in milktea_flavor_name:
    print("-", i)
print("Ice Coffee Flavor")
for i in icecoffee_flavor_name:
    print("-", i)
print("       Total Price   ₱", float(total_price))

while True:
    cash = float(input("\nEnter Cash\n="))
    if cash < total_price:
        print("\nNot Enough Money\n")
    else:
        print("\n\n-----Thank You For Your Order-----\n")
        total = cash - total_price
        print("Ice Coffee Flavor")
        for i in icecoffee_flavor_name:
            print("-", i)
        print("Milk Tea Flavor")
        for i in milktea_flavor_name:
            print("-", i)
        print("       Total Price   ₱", float(total_price))
        print("              Cash   ₱", float(cash))
        print("            Change   ₱", float(total))
        print("\n-----Payment Successful-----")
        break
