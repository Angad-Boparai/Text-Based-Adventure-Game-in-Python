from room import Room
from character import Enemy

kitchen=Room("Kitchen")
kitchen.set_description("Smelly place, buzzing with flies")

ballroom=Room("Ballroom")
ballroom.set_description("Dusty and scary place")

dining_hall=Room("Dining Hall")
dining_hall.set_description('Dark and dainty place')

kitchen.link_room(dining_hall,'South')
dining_hall.link_room(ballroom,'West')
dining_hall.link_room(kitchen,'North')
ballroom.link_room(dining_hall, "East")

dave=Enemy("Dave","He seems to be a weird guy.")
dave.set_conversation('Hi, my name is Inigo Montoya. You killed my father. Prepare to die.')
dave.set_weakness("Cheese")

current_room=kitchen

while True:
	current_room.get_details()
	command=input("> ")
	current_room=current_room.move(command)