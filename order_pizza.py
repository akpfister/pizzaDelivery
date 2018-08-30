#!/usr/bin/python

# Using pizzapi package from https://github.com/gamagori/pizzapi
from pizzapi import *

# HELPER FUNCTIONS

def get_address(): 
	print("We need your delivery address to get started.\n")
	street = input("Street: ")
	city = input("City: ")
	state = input("State: ")
	zip_code = input("Zip code: ")
	address = Address(street, city, state, zip_code)
	return address

def get_contact_info(filler):
	print("Next we need some contact info.\n")
	first = input("First name: ")
	last = input("Last name: ")
	email = input("Email: ")
	cust = Customer(first, last, email, filler)
	return cust

# MAIN PROMPT

print("Welcome to my pizza delivery script.\nOrders will be made using Dominos Pizza.\n")

# Retrieves address
while True:
	address = get_address()
	print('\n' + address.line1)
	print(address.line2 + '\n')
	correct = input("Does this information look correct? (y/n): ")
	if correct == 'y':
		print("\nAwesome, let's continue.\n")
		break

# Retrieves contact information
while True:
	customer = get_contact_info(address)
	print('\n' + customer.first_name + '\n') #add function to cleanly print details
	correct = input("Does this information look correct? (y/n): ")
	if correct == 'y':
		print("\nAwesome, let's continue.\n")
		break

# Finds closest store to address
store = address.closest_store()
print("The closest store to your address is:\n")
print(str(store.data) + '\n') #prints some data about the closest store

# Gets menu and asks if the user wants the whole menu or just search
menu = store.get_menu()
while True:
	menu_choice = input("Type 'see menu', enter an item to search or 'done': ")
	if menu_choice == 'done':
		break
	if menu_choice == 'see menu':
		print(menu.display()) #prints entire menu with codes
	if str(menu.search(Name=menu_choice)) == 'None':
		print("No results shown. Please try searching another item.\n")
	else: 
		print(str(menu.search(Name=menu_choice)))

# Gets order together for the user
order = Order(store, customer, address)
while True:
	order_choice = input("Would you like to add or remove an item? ")
	if order_choice == 'q':
		break
	if order_choice == 'add':
		item = input("Enter an item to add to the order: ")
		order.add_item(item)
	if order_choice == 'remove':
		item = input("Enter an item to remove from the order: ")
		order.remove_item(item)
	print(order.data)
	print('\n' * 2)

# This is to validate the order and give a price
print("We are validating the order.")
validated = order.validate()
print(validated)

price = order.urls.price_url()

print(price)

print("Simulation over")
	
"""
# Gets card information ready for payment
while True:
	card_nu = input("Please enter the number of the card: ")
	exp = input("Expiration date: ")
	back_digits = input("CVV info: ")
	zipcode = input("Zipcode: ")
	print("Card number: " + card_nu + "\nExpiration Date: " + exp + "\nCVV: " + back_digits + "\nZipcode: " + zipcode)
	correct = input("Does this information look correct? (y/n): ")
	if correct == 'y':
		payment = PaymentObject(card_nu, exp, back_digits, zipcode)
		break
"""

"""
# Places order
correct = input("Are you ready to place your order? (y/n): "
if correct == 'y':
	response = order.place(payment)
	print(response)
"""

"""
# Set to not let prompt end
while True:
	print("Now we wait for your order")
	pizza = input("Enter q when pizza arrives")
	if pizza == 'q':
		break
"""

"""
# Testing

address = get_address() 

print('\n' * 5)
print(address.line2) #prints the whole address

customer = get_contact_info(filler = address)

print(customer.first_name)

store = address.closest_store()

print('\n' * 5)
print(store.data) #prints some data about the closest store

menu = store.get_menu()

print('\n' * 5)
print(menu.display()) #prints entire menu with codes
"""
