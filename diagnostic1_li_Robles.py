def  calculate_checkout(cart_total, shipping_speed):
    cart_total = float(input("Enter cart total: "))
    shipping_speed = input("Enter shipping choice (express/overnight/standard): ")
    if shipping_speed == "express":
        cart_total = cart_total + 15
        print("Your shipping fee is $15 and your total is ($): ")
    elif shipping_speed == "overnight":
        cart_total = cart_total + 25
        print("Your shipping fee is $25 and your total is ($): ")
    elif shipping_speed == "standard":
        cart_total = cart_total + 10
        print("Your shipping fee is $10 and your total is ($): ")
    else:
        print("Invalid shipping choice.")

    return cart_total


print((calculate_checkout(1000,"express"))) 
