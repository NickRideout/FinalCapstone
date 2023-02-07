from tabulate import tabulate


#========The beginning of the class==========

# It creates a class called Shoes.
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def get_country(self):
        return self.country

    def get_code(self):
        return self.code
    
    def get_product(self):
        return self.product

    def set_quantity(self, new_quant):
        self.quantity = new_quant

    def __str__(self):
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}\n".upper()

#=============Shoe list===========

# Opening the file in read and write mode.
inventory_read = open("inventory.txt", "r")
inventory_write = open("inventory.txt", "a+")

# Creating two empty lists.
shoe_list = []
shoe_obj = []

#==========Functions outside the class==============

def read_shoes_data():
   

    file = None

    try:
       # This is reading the file and splitting the lines into a list.
        for lines in inventory_read:
            strip_lines = lines.strip("\n")
            split_lines = strip_lines.split(",")
            shoe_list.append(split_lines)

       # This is creating a list of objects.
        for i in range(1, len(shoe_list)):
            array = shoe_list[i]
            shoe1 =  Shoe(array[0], array[1], array[2], array[3], int(array[4]))
            shoe_obj.append(shoe1)

#It is trying to open the file and if it fails, it will print the error message.
    except FileNotFoundError as error:
        print("\nSorry, this file does not exist!\n")
        print(error)

   # Closing the file.
    finally:
        if file is not None:
            file.close()

def capture_shoes():
    
    file = None

    try:
        # This is asking the user to input the country, code, product, cost and quantity of the product.

        new_country = input("Please enter the country of your product:\n")
        new_code = input("Please enter the code of your product:\n")
        new_product = input("Please enter the name of your product:\n")
        new_cost = int(input("Please enter the cost of your product, only in numbers. E.g. 12345\n"))
        new_quantity = int(input("Please enter the quantity of your product, only in numbers. E.g. 2\n"))

       # Creating a new object called new_shoe and then appending it to the list shoe_obj.
        new_shoe = Shoe(new_country, new_code, new_product, new_cost, new_quantity)
        shoe_obj.append(new_shoe)

       # This is writing the new product to the file.
        inventory_write.write(f'\n{new_country},{new_code},{new_product},{new_cost},{new_quantity}')
        print("\nThank you, your product has been loaded!\n")

        inventory_write.close()

    except FileNotFoundError as error:
        print("\nSorry, this file does not exist!\n")
        print(error)

    finally:
        if file is not None:
            file.close()

def view_all():

    file = None
    
    try:

        print("\n---------------------------------------------STOCKLIST---------------------------------------------\n")

        # Creating empty lists.
        country = []
        code = []
        product = []
        cost = []
        table  = []
        quantity = []

        # Creating a list of all the countries, codes, products, costs and quantities.
        for lines in shoe_obj:
            country.append(lines.get_country())
            code.append(lines.get_code())
            product.append(lines.get_product())
            cost.append(lines.get_cost())
            quantity.append(lines.get_quantity())

        table = zip(country, code, product, cost, quantity)

        print(tabulate(table, headers = ('Country','Code', 'Product', 'Cost', 'Quantity'), tablefmt='fancy_grid'))

        print("\n---------------------------------------------END-------------------------------------------------\n")

    except FileNotFoundError as error:
        print("\nSorry, this file does not exist!\n")
        print(error)

    finally:
        if file is not None:
            file.close()

def restock():

    file = None

    restock_list = []
    country = []
    code = []
    product = []
    cost = []
    quantity = []
    table  = []

    try:
       # Sorting the list of objects by the quantity.
        shoe_obj.sort(key=lambda x:x.quantity)

       # Appending the first 5 items in the list to the restock_list.
        for i in range(1,6):
            restock_list.append(shoe_obj[i])
    
        print("\n----------------------------Lowest stock items:----------------------------\n")

        for line in restock_list:
            country.append(line.get_country())
            code.append(line.get_code())
            product.append(line.get_product())
            cost.append(line.get_cost())
            quantity.append(line.get_quantity())

        table = zip(country, code, product, cost, quantity)

        print(tabulate(table, headers = ('Country','Code', 'Product', 'Cost', 'Quantity'), tablefmt='fancy_grid', showindex= range(1,6)))
        
        print("\n---------------------------------------------------------------------------\n")

        # This is asking the user to input the index of the product they want to restock and the new quantity.
        user_input_item = int(input("\nPlease confirm the index of the product you want to restock:\n"))
        user_input_qty = int(input("\nPlease confirm the new quantity:\n"))
        shoe_obj[user_input_item].set_quantity(user_input_qty)

        output = ''
        # Creating a string of all the items in the list shoe_obj.
        for item in shoe_obj:
            output += (f'{item.get_country()},{item.get_code()},{item.get_product()},{item.get_cost()},{item.get_quantity()}\n')

        inventory_write_test = open("inventory.txt", "w")
        inventory_write_test.write(output)
        inventory_write_test.close()

        print("\nYour product has been updated!")

    except FileNotFoundError as error:
        print("\nSorry, this file does not exist!\n")
        print(error)

    finally:
        if file is not None:
            file.close()

def search_shoe():

    search_shoe = input("\nPlease enter the code you are searching for:\n\n")

    # Searching for the code that the user has entered and then printing the line that contains that code.
    for line in shoe_obj:
        if line.get_code() == search_shoe:
            print(f'\n {line}')

    print("\nPlease select another option from the menu below\n")


def value_per_item():

 # Multiplying the cost and quantity of each item and then printing the code and the value of each item.
    for line in shoe_obj:
        value = int(line.get_cost()) * int(line.get_quantity())
        print(f'{line.get_code()} VALUE: R{value}\n')

def highest_quantity():

    highest_qty = []

  # Creating a list of all the items in the list shoe_obj.
    for line in shoe_obj:
        highest_qty.append(line)

    print("\n----------------------------Highest stock item:----------------------------\n")

    print(max(shoe_obj, key=lambda item: item.quantity))
    print("\nThis item has now been marked on sale\n")
    print("\nPlease select an option from the menu below")


#==========Main Menu=============

read_shoes_data()


while True:

    try:
       # Asking the user to select an option from the menu.
        menu = int(input('''\n
            Welcome to HyperionDev Inventory System! 
            Please select from the menu below:
            1. Capture Shoes
            2. View All
            3. Restock
            4. Search
            5. View Item Values
            6. View Sale Items
            \n'''))

        if menu == 1:
            capture_shoes()

        elif menu == 2:
            view_all()

        elif menu == 3:
            view_all()
            restock()

        elif menu == 4:
            search_shoe()

        elif menu == 5:
            value_per_item()

        elif menu == 6:
            highest_quantity()

        elif menu > 6:
            print("\nYou have selected an invalid option. Please try again by choosing from the menu below.\n")

    except ValueError:
        print("\nYou have selected an invalid option. Please try again by entering a number.\n")
        
# ====================================================== END =============================================== #
