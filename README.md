# Stock Management

This script in Python simulates the Stock Management System for the manager in Nike warehouse using files and Object Oriented Programming (OOP). It lets the manager to add a stock, look at all the stock, search for a product by code, determine the product with the lowest quantity and restock it, determine the product with highest quantity and announce sale on them and calculate the total value of each stock.

# Contents

| Command | Description |
| --- | --- |
| Installation | Lists any installations and requirements for the project |
| Functions | Short cuts to explanations to certain functions |
| Usage | Explanation on how to use the app |

# Installation 

The application expects inventory.txt to be in the same folder as the script. The application is dependent on the tabulate module which could be installed by, pip install tabulate. Copy all the files from this folder and execute inventory.py

# Functions 

| Command | Description |
| --- | --- |
| Capture Shoes | This takes user input about a shoe and adds it to the stock list |
| View All | This lets the user to view all the shoes stocks from inventory |
| Restock | This lets the user to update the stock entry for the shoes with the lowest stock in the inventory |
| Search | This lets the user to search for a shoe from the inventory file based on code |
| View Item Values | This displays the stock values of all the shoes in the inventory |
| View Sale Items | This displays items that are currently on sale |

# Usage
# Menu
![menu](https://user-images.githubusercontent.com/109149306/217335699-583c1fdd-db37-4a1c-add1-24f156a83db4.jpg)

The program loads with the start screen with the above options.

# Capture Shoes
![captureshoes](https://user-images.githubusercontent.com/109149306/217335806-a32d7e4f-51e1-416e-b45b-879208ac115d.jpg)

Takes the input and adds the new shoe to the stock list

# View All
![VA1](https://user-images.githubusercontent.com/109149306/217335831-77b9695a-7ff2-4b9a-adf5-5e573ca6342f.jpg)
![VA2](https://user-images.githubusercontent.com/109149306/217335843-e5cf37ac-6000-485e-bf5c-0fe36028e2cc.jpg)

This option lets the user to view all the shoe stocks from the inventory.txt file in a table format.

# Restock
![RS](https://user-images.githubusercontent.com/109149306/217335869-518944a8-1ef0-4063-85d2-6dedfd558896.jpg)

This option displays the shoes with lowest entries and asks the user to top up the stock values for those shoe entries. It updates the entries for those shoes in inventory.txt

# Search 
![S](https://user-images.githubusercontent.com/109149306/217335883-74edb298-be53-441d-9857-ad3312005f7d.jpg)

This option allows the user to serach for a specific shoe.

# View Item Values
![VIV](https://user-images.githubusercontent.com/109149306/217335892-29e51a0d-84b7-4a6d-a7c2-d446eaa33baa.jpg)

This option calculates the stock value for each stock from the inventory.txt and displays the value along with product, code, quantity and cost.

# View Sale Items
![VSI](https://user-images.githubusercontent.com/109149306/217335904-9d6ff94e-0456-4ac0-9402-16bb22e728b2.jpg)

This option allows the user to see all the shoes that are currently on sale.
