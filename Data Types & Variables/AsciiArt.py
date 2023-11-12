# Final Program
# Programmer: Olmedo, Johnny
# ITS-320
# Submission date: 1/16/2022
# This program is an automobile inventory program, able to add, delete, and modify attributes
from operator import index, inv
from tkinter import Menu
from typing import Dict
from xml.dom.minidom import Element

class Automobiles:
    def __init__(self, make, model, color, year, mileage):
        # private make member
        self.__make = make
        # private model member
        self.__model = model
        self.__color = color
        self.__year = year
        self.__mileage = mileage 

    # private init method
    # public make setter
    def set_make(self, make):
        self.__make = make
    def set_model(self, model):
        self.__model = model
    def set_color(self, color):
        self.__color = color
    def set_year(self, year):
        self.__year = year
    def set_mileage(self, mileage):
        self.__mileage = mileage

    def get_make(self):
        return self.__make
    def get_model(self):
        return self.__model
    def get_color(self):
        return self.__color   
    def get_year(self):
        return self.__year
    def get_mileage(self):
        return self.__mileage

# function that adds new vehicles -------------------------------------------------------------
def add_vehicle(inventory):		
    # get the make of the car
    car_make = input("please enter the make of the car: ")
    # get the model
    car_model = input("please enter the model of the car: ")
    # get the color
    car_color = input("please enter the color of the car: ")
    # get the year
    car_year = input("please enter the year the car was made: ")
    # get the mileage
    car_mileage = input("please enter the mileage of the car: ")    
    # create an instance named vehicles    
    vehicles = Automobiles(car_make, car_model, car_color, car_year, car_mileage)
    vehicles.set_make(car_make) # set make
    vehicles.set_model(car_model) # set model
    vehicles.set_color(car_color) # set color
    vehicles.set_year(car_year) # set year
    vehicles.set_mileage(car_mileage) # set mileage
    # add vehicles to the inventpry list
    inventory.append(vehicles)
    # format the string and print it out
    format(inventory)
    # return inventory
    return inventory

# function that deletes a cars in inventory -------------------------------------------------------    
def delete_vehicle(inventory):
    if len(inventory) == 0:
        print("Vehicle inventory is empty") 
        return inventory

    # call format function to print out what the inventory looks like
    format(inventory)
    delete = input("which vehicle would you like to delete? (use numbers to identify vehicle) ")
    # - 1 to match elements
    choice = int(delete) - 1
    # as long as choice isn't less than the len of inventory
    if choice < len(inventory):
        # delete the users choice
        del inventory[choice]
    else:
        print("you didn't put a valid entry")
    # show what the inventory looks like now
    format(inventory)
    # return inventory
    return inventory

# function updates the inventory ------------------------------------------------------------------------------
def update_vehicle(inventory): 
    # if theres nothing in the inventory
    if len(inventory) == 0:
        print("Vehicle inventory is empty") 
        return inventory
    format(inventory) # print inventory
    # choose which one to update
    update = input("which vehicle would you like to update? (use numbers to identify vehicle) ")
    choice = int(update) - 1 # let choice reflect the elements in the list
    if choice < len(inventory):
        # update the car details for everything
        car_make = input("please enter the make of the car: ")
        car_model = input("please enter the model of the car: ")
        car_color = input("please enter the color of the car: ")
        car_year = input("please enter the year the car was made: ")
        car_mileage = input("please enter the mileage of the car: ") 
        # set the new details
        inventory[choice].set_make(car_make)
        inventory[choice].set_model(car_model)
        inventory[choice].set_color(car_color)
        inventory[choice].set_year(car_year)
        inventory[choice].set_mileage(car_mileage)
    else:
        print("you didn't put a valid entry")
    # print   
    format(inventory)
    return inventory

# this function prints out inventory and writes to the file --------------------------------------------------
def format(inventory):
    # write to file
    vehicle_file = open('vehicle.txt', 'w+')
    vehicle_file.write('\n----------------')
    vehicle_file.write('\n   INVENTORY')
    vehicle_file.write('\n----------------')

    #print
    print('----------------')
    print('   INVENTORY')
    print('----------------')

    # go threw and write everything in the inventory to the file
    for i in inventory:
        # set the element to keep track of vehicle number
        element = inventory.index(i) + 1
        # write to the file
        vehicle_file.write('\nVehicle #%d' % (element))
        # print it to the program
        print('Vehicle #%d' % (element))
        # write it to the file in the correct format
        vehicle_file.write('\n make : {0}'.format(i.get_make()))
        vehicle_file.write('\n model : {0}'.format(i.get_model()))
        vehicle_file.write('\n color : {0}'.format(i.get_color()))
        vehicle_file.write('\n year : {0}'.format(i.get_year()))
        vehicle_file.write('\n mileage : {0}'.format(i.get_mileage()))

        # print it for the program
        print('make : {0}'.format(i.get_make()))
        print('model : {0}'.format(i.get_model()))
        print('color : {0}'.format(i.get_color()))
        print('year : {0}'.format(i.get_year()))
        print('mileage : {0}'.format(i.get_mileage()))
    # close
    vehicle_file.close()

# menu function -------------------------------------------------------------------------------------
def create_menu():
    print('\n----------------')
    print('     MENU')
    print('----------------')
    menu = {}
    menu['1']="Add Vehicle." 
    menu['2']="Delete Vehicle."
    menu['3']="Update Attributes"
    menu['4']="Exit"
    # format the menue
    for x, v in menu.items():
        # print the first argument, then the second one after 
        print(f' {x}: {v}') 
    print('\n')
    return menu

# this function lets the user choose what they want to do -------------------------------------------------
def choose():
    # initilize a list
    vehicle_inventory = []
    user=True
    while user:
        create_menu()
        ans=input("What would you like to do? ") 
        # add vehicle
        if ans=="1": 
            add = add_vehicle(vehicle_inventory)
        # delete vehicle
        elif ans=="2":
            delete = delete_vehicle(vehicle_inventory)
        # update attributes
        elif ans=="3":
            update = update_vehicle(vehicle_inventory)
        # quit
        elif ans == "4":
            print("\n Goodbye")
            break
        elif ans !="":
            print("\n Invaild Entry")
        

def main():
    # getuser choice
    user_choice = choose()
main() # call main