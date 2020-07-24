from character import Character
from character import Enemy

dave=Enemy('Dave','He seems to be a weird guy.')

dave.describe()

dave.set_conversation('Hi, my name is Inigo Montoya. You killed my father. Prepare to die.')

dave.talk()

dave.set_weakness("cheese")

print("What will you fight with ?")
item_chosen=input()
dave.fight(item_chosen)