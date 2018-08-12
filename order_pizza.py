#!/usr/bin/python

# Using pizzapi package from https://github.com/gamagori/pizzapi
from pizzapi import *

#helper functions

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

#show information based on what was given	

"""
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

# Main Prompt

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
	menu_choice = input("Type 'see menu' or enter and item to search: ")
	if menu_choice == 'see menu':
		print(menu.display()) #prints entire menu with codes
		break
	# if menu.search(menu_choice) == '':
		# print("No results shown.\n")
	print(str(menu.search(menu_choice)))


