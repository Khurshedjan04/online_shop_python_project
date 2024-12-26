class OnlineShope:
    def __init__(self):
        self.products = []
        self.__users = []
        self.__sold_products = 0

    def admin_dashboard(self, nickname, password):
        if nickname == "admin" and password == "admin":
            return True

    def add_product(self, product, quantity):
        self.products.append({
            "name": product.name,
            "price": product.price,
            "quantity": int(quantity)
        })

    def remove_product(self, product):
        for i in self.products:
            if i["name"] == product:
                self.products.remove(i)
                print("Product removed!")
                break
        else:
            print("Product not found!")

    def show_products(self):
        for i in self.products:
            if i["quantity"] > 0:
                print(f"Product name: {i['name'].upper()}, Product price: {i['price']},Product availability: {i['quantity']}")


    def sell_product(self, user, product, quantity):
        for i in self.products:
            if i["name"] == product:
                if i["quantity"] >= quantity:
                    i["quantity"] -= quantity
                    user.add_to_cart(product, quantity, i["price"])
                    print(f"Success! You added {quantity} units of {product}(s) to your cart.")
                else:
                    print(f"Sorry, we don't have that much {product} in stock. Available quantity: {i['quantity']}")
                    break

    def calculate_sold_products(self, quantity):
        self.__sold_products += int(quantity)

    def show_products_sold(self):
        print(f"Total sold products: {self.__sold_products}")

    def fill_user_ifo(self):
        user = input("Enter your name: ")
        password = input("Enter your password: ")
        gender = input("Enter your gender: ")
        return user, password, gender

    def add_user(self, user):
        self.__users.append(user)

    def remove_user(self, user):
        self.__users.remove(user)

    def get_users(self):
        return self.__users
        

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = int(price)


class Users:
    def __init__(self, name, pasword, gander, balance = 0):
        self.__name = name
        self.__pasword = pasword
        self.__gender = gander
        self.__balance = balance
        self.__cart = []
        self.__orders = []
    
    def get_full_info(self):
        return f"{self.__name} {self.__surname}\nBorn year: {self.__born_year}\nGender: {self.__gender}\nBalance: {self.__balance}"
    
    def show_cart(self):
        for i in self.__cart:
            for j, k in i.items():
                for l, m in k.items():
                    print(f"Product: {j.upper()}|  Quantity: {l} | Price: {m}")
    
    def get_cart(self):
        return self.__cart
    
    def get_balance(self):
        return self.__balance

    def add_balance(self, amount):
        self.__balance += int(amount)

    def withdraw(self, amount):
        self.__balance -= int(amount)

    def add_to_cart(self, product, quantity, price):
            for item in self.__cart:
                for existing_product, details in item.items():
                    if existing_product == product:
                        existing_quantity, existing_price = next(iter(details.items()))
                        details.clear()
                        details[existing_quantity + quantity] = price
                        return 
            self.__cart.append({product: {quantity: price}})


    def remove_from_cart(self, product):
        self.__cart.remove(product)

    def calculate_total_cart_price(self):
        total_price = 0
        total_quantity = 0
        for item in self.__cart:
            for product_details in item.values():
                for quantity, price in product_details.items():
                    total_price += price * quantity
                    total_quantity += quantity
        return total_price, total_quantity

    def make_order(self):
        if self.__cart == []:
            print("Your cart is empty.")
            return 0
        total_price, total_quantity = self.calculate_total_cart_price()
        if self.__balance < total_price:
            print(f"Your total is {total_price}. You don't have enough money to make this order.")
            return 0
        else:
            self.withdraw(total_price)
            print(f"Success! You made an order for {total_price} sum.")
        self.__orders.append(self.__cart)
        self.__cart = []
        return total_quantity

    def get_full_info(self):
        return f"{self.__name} {self.__surname}\nBorn year: {self.__born_year}\nGender: {self.__gender}\nBalance: {self.__balance}"
    
    def show_cart(self):
        for i in self.__cart:
            for j, k in i.items():
                for l, m in k.items():
                    print(f"Product: {j.upper()}|  Quantity: {l} | Price: {m}")
    
    def get_cart(self):
        return self.__cart
    
    def get_orders(self):
        return self.__orders
                
    def show_orders(self):
        print("Your orders:")
        for order in self.__orders:
            for i in order:
                for j, k in i.items():
                    for l, m in k.items():
                        print(f"Product: {j.upper()}|  Quantity: {l} | Price: {m}")


shop = OnlineShope()
product1 = Product("apple", 5000)
product2 = Product("banana", 2000)
product3 = Product("orange", 3000)
product4 = Product("lemon", 4000)
product5 = Product("kiwi", 6000)

shop.add_product(product1, 20)
shop.add_product(product2, 3)
shop.add_product(product3, 7)
shop.add_product(product4, 9)
shop.add_product(product5, 11)

def admin():
    print("Welcome to admin dashboard!")
    admin_nickname = input("Enter admin nickname: ")
    admin_password = input("Enter admin password: ")
    if shop.admin_dashboard(admin_nickname, admin_password):
        print("Success, loged in!")
        while True:
            choose = input(f"1. Show products\n2. Add product\n3. Remove product\n4. See how many products were sold\n5. Back to UI\nEnter your choice: ")
            if choose == "1":
                shop.show_products()
            elif choose == "2":
                product = input("Enter product name: ")
                price = int(input("Enter product price: "))
                quantity = int(input("Enter product quantity: "))
                shop.add_product(Product(product, price), quantity)
                print("Product added!")
            elif choose == "3":
                product = input("Enter product name: ")
                shop.remove_product(product)
            elif choose == "4":
                shop.show_products_sold()
            elif choose == "5":
                break
            else:
                print("Invalid input!")
    else:
        print("Wrong nickname or password!")


def main():
    print(f'welcome to our Shop!\nWhat are you up to do today?')
    while True:
        choose = input(f"1. Show products\n2. Buy Products\n3. Show my cart\n4. Show my orders\n5. Login\n6. Log out\n7. Exit\n8. Admin Dashboard\nEnter your choice: ")
        if choose == "1":
            shop.show_products()
        elif choose == "2":
            if shop.get_users() == []:
                print(f"You are not logged in!")
                while True:
                    choose2 = input(f"Would you like to log in now? (y/n):")
                    if choose2.lower() == "y" or choose2 == "yes":
                        user, password, gender = shop.fill_user_ifo()
                        user1 = Users(user, password, gender)
                        shop.add_user(user1)
                        print("Success, loged in!")
                        break
                    elif choose2.lower() == "n" or choose2 == "no":
                        print("You can look at products but you can't buy them if you are not loged in!")
                        break
                    else: 
                        print("Invalid input!")
            elif user1 in shop.get_users():
                while True:
                    product = input(f"Enter product name: ")
                    for i in shop.products:
                        if i["name"] == product and i["quantity"] > 0:
                            print("Lucky boy, we have that product!")
                            print(f"Product name:{product}\nProduct price: {i['price']}\nProduct availability: {i['quantity']}")
                            quantity = int(input("How many would you like to add to your cart:"))
                            shop.sell_product(user1, product, quantity)
                            choose3 = input("Would you like to add another product? (y/n):")
                            break
                    else:
                        print("Sorry, we don't have that product in our shop!")
                        choose3 = input("Would you like to add other product? (y/n):")
                    if choose3.lower() == "n" or choose3 == "no":
                        break
                    elif choose3.lower() == "y" or choose3 == "yes":
                        continue
                    else:
                        print("Assuming you mean 'Yes'!")
            else:
                print("You are not loged in!")
        elif choose == "3":
            if shop.get_users() == []:
                print(f"You are not loged in!\nPlease log in first!")
                continue
            if len(user1.get_cart()) > 0:
                print(f"Your cart:")
                user1.show_cart()
                print(f'Your balance: {user1.get_balance()}')
                while True:
                    if user1.get_balance() != 0:
                        choose4 = input("Would you like to make an order? (y/n):")
                        if choose4 == "y" or choose4 == "yes":
                            quantity = user1.make_order()
                            shop.calculate_sold_products(quantity)
                            if quantity != 0:
                                break
                            print(f'Your balance: {user1.get_balance()}')
                        elif choose4 != "n" and choose4 != "no":
                            print("Assuming you mean 'Yes'!")
                            quantity = user1.make_order()
                            shop.calculate_sold_products(quantity)
                            if quantity != 0:
                                break
                            print(f'Your balance: {user1.get_balance()}')
                        else:
                            break
                    if len(user1.get_cart()) != 0 and user1.get_balance() < user1.calculate_total_cart_price()[0]:
                        choose5 = input("Would you like to pop up your balance to make an order: (y/n)")
                        if choose5.lower() == "y" or choose5 == "yes":
                            amount = input("Enter amount: ")
                            user1.add_balance(amount) 
                            print(f'Your balance: {user1.get_balance()}')
                        elif choose5.lower() == "n" or choose5 == "no":
                            break
                        else:
                            print("Assuming you mean 'No'!")
                            break               
            else:
                print("Your cart is empty!")
        elif choose == "4":
            if shop.get_users() == []:
                print(f"You are not loged in!\nPlease log in first!")
                continue
            if len(user1.get_orders()) == 0:
                print("You have no orders!")
            else:
                user1.show_orders()
        elif choose == "5":
            if shop.get_users() == []:
                print(f"Logging you in...")
                user, password, gender = shop.fill_user_ifo()
                user1 = Users(user, password, gender)
                shop.add_user(user1)
                print("Success, loged in!")
            elif user1 in shop.get_users(): 
                print("You are already loged in!")
        elif choose == "6":
            if shop.get_users() == [] or user1 not in shop.get_users():
                print("If you are not loged in, how can you log out?!")
            elif user1 in shop.get_users():
                shop.remove_user(user1)
                print("Success, loged out!")
        elif choose == "7":
            print("Goodbye! Have a nice day!")
            break
        elif choose == "8":
            admin()
        else:
            print("Invalid input!")
main()