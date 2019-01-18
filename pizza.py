#!/usr/bin/python

# Using pizzapi package from https://github.com/gamagori/pizzapi
from pizzapi import *

class Pizza(object):
    def __init__(self, address, customer, store):
        self.address = address
        self.customer = customer
        self.store_location = store
        self.order = None
        self.payment = None

    def see_menu(self):
        print("The closest store to you is " + str(self.store_location.data) + '\n')
        menu = self.store_location.get_menu()
        print("Here is the menu (NOTE: not all the items exist/can be added to the order and I don't know why):\n")
        print(menu.display())
        find = input("Would you like to 'search' for an item? ")
        if find == 'search':
            print("Enter 'q' to exit.\n")
            item = ''
            while item != 'q':
                item = input("Enter something to search: ")
                if str(menu.search(Name=item)) == 'None':
                    print("No results shown. Please try searching another item.\n")
                else:
                    print(str(menu.search(Name=item)))

    def make_order(self):
        self.order = Order(self.store_location, self.customer, self.address)
        manipulate = ''
        print("Enter 'done' when finished ordering or 'see order' to view order.")
        while manipulate != 'done':
            manipulate = input("Would you like 'add' or 'remove' and item? ")
            if manipulate == 'add':
                item_add = input("Enter the code of the item to add: ")
                try:
                    self.order.add_item(item_add)
                except:
                    print("Sorry that code did not work, please try another one.\n")
            elif manipulate == 'remove':
                item_remove = input("Enter the code of the item to remove: ")
                try:
                    self.order.remove_item(item_remove)
                except:
                    print("That code was not on the order, please try again.\n")
            else:
                print("Here is your order so far:\n")
                print(self.order.data)
                price = self.order.urls.price_url()

    def card_info(self):
        print("Enter your car information to pay for the order.")
        correct = ''
        while correct != 'yes':
        	card_nu = input("Please enter the number of the card: ")
        	exp = input("Expiration date: ")
        	back_digits = input("CVV info: ")
        	zipcode = input("Zipcode: ")
        	print("Card number: " + card_nu + "\nExpiration Date: " + exp + "\nCVV: " + back_digits + "\nZipcode: " + zipcode)
        	correct = input("Does this information look correct? (yes/no): ")
        	if correct == 'yes':
        		self.payment = PaymentObject(card_nu, exp, back_digits, zipcode)
        		break

    def place_order(self):
        ready = input("Are you ready to place your order? (yes/no)" )
        if ready == 'yes':
            response = self.order.place(self.payment)
            print(response)
