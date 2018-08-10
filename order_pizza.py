#!/usr/bin/python

from pizzapi import *

#helper functions

def get_address(): 
	print("We need your delivery address to get started.")
	street = input("Street: ")
	city = input("City: ")
	state = input("State: ")
	zip_code = input("Zip code: ")
	address = Address(street, city, state, zip_code)
	return address

def get_contact_info(filler):
	print("Next we need some contact info")
	first = input("First name: ")
	last = input("Last name: ")
	email = input("Email: ")
	cust = Customer(first, last, email, filler)
	return cust

#show information based on what was given	

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

# Main Prompt

print("Welcome to my pizza delivery script. \n Orders will be made using Dominos Pizza.")

# address = get_address()

print(address.line2)
correct = input("Does this information look correct? (y/n): ")

