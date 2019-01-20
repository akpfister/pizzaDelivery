#!/usr/bin/python

from pizzapi import *
from pizza import Pizza

# HELPER FUNCTIONS
def get_address():
	print("We need your delivery address to get started.\n")
	street = input("Street: ")
	city = input("City: ")
	state = input("State: ")
	zip_code = input("Zip code: ")
	address = Address(street, city, state, zip_code)
	return address

def get_contact_info(addr):
	print("Next we need some contact info.\n")
	first = input("First name: ")
	last = input("Last name: ")
	email = input("Email: ")
	phone = input("Phone number: ")
	cust = Customer(first, last, email, phone, addr)
	return cust

print("Welcome to my pizza delivery script, orders will be made using Dominos Pizza.\n")

# Retrieves address
correct = 'n'
while correct == 'n':
	address = get_address()
	print('\n' + address.line1)
	print(address.line2 + '\n')
	correct = input("Does this information look correct? (y/n): ")
	# if correct == 'y':
    #   break

correct = 'n'
# Retrieves contact information
while correct == 'n':
	customer = get_contact_info(address)
	print('\n' + customer.first_name + ' ' + customer.last_name + '\n' + customer.email + '\n' + customer.phone + '\n') #add function to cleanly print details
	correct = input("Does this information look correct? (y/n): ")

# Finds closest store to address
print("Getting store.\n")
store = address.closest_store()

#initialize Pizza object used to carry out ordering sequence
print("Making Pizza object.\n")
domino = Pizza(address, customer, store)

#displays menu
domino.see_menu()

#add/remove items for an order
domino.make_order()

#payment information
domino.card_info()

#when ready, will place the order
# domino.place_order()
