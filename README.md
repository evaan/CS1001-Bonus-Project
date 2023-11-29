# CS1001 Bonus Project: Basic Characters/Inventories
This is a project that is inspired by Runescape, which was intended to be a lot smaller and simpler than it ended up being.
## Superclasses
This project contains two superclasses, with them being an Item, and Character
### Item
The item superclass has a total of 4 functions:
 - `__init__(name: str, description: str)`: This function gets the name and description of the object, and sets them to their respective variables.
 - `getName()`: This function returns the item name (`self.__name`).
 - `getDescription()`: This function returns the description (`self.description`).
 - `__str__()`: Processes the function into a string with the structure:
 ```
 Stats:
 Name: {name}
 Description: {description}
 ```
### Character
 This class contains 23 different functions:
 - `__init__(name: str, hitpoints: int, melee: int, ranged: int, magic: int)`: Appends itself to a list of characters (used for some abilities I created later), alongside assigning the characrters name, hitpoints, melee stat, ranged stat, mage stat which were recieved as arguments to their appropriate variable. It also creates an empty inventory and armour list/dictionary. Each player has 5 total inventory spaces, alongside equipment slots for their Weapon, Helmet, Chest, Legs, Boots, and a Cape.
 - `getName()`: Returns the characters name
 - `setName(str)`: Sets the characters name
 - `getHitpoints()`: Gets the charactesr hitpoints
 - `removeHitpoints(int)`: Rather than a set hitpoints, I've added a remove/add hitpoint system, if the user has equal to less than 0 HP it will announce their unfortunate death, while also announcing their HP loss.
 - `addHitpoints(int)`: Similar to `removeHitpoints(int)`, this function announces the characters HP gain and adds it to the HP value.
 - `getMelee/getRanged/getMagic()`: Accessor for the respective stat.
 - `boostMelee/drainMelee/boostRanged/drainRanged/boostMagic/drainMagic(int)`: Boosts or drains the respective stat, while announcing it.
 - `getInventory()`: Returns a list of the itmes in all non empty inventory slots with the structure:
 ```
 {name}'s Inventory: {ITEM}, {ITEM}, {ITEM}, {ITEM}, {ITEM}
 ```
 - `addItem(Item)`: Adds an `Item` to the players inventory if there is room, and announce it to the player. If the item cannot fit it will announce that the player has no room.
 - `dropItem(str)`: Drop an item if the name is found in the inventory while announcing it, otherwise inform the user an item could not be found with that name.
 - `getItems()`: Returns a list of all items that the character has equipped with the structure:
 ```
 Weapon:
 Helmet: 
 Chestpiece:
 Leggings:
 Boots:
 Cape:
 ```
 - `equipItem(Item)`: Equips the item if it can be found in the players inventory, if it cannot be found it will inform the player, and if there is an item in that slot already equipped it will inform the player.
 - `unequipItem(str)`: Goes through armour slots trying to unequip an item, if an item with that name is found it will then attempt to unequip it and put it in the inventory if they have room, otherwise it will do nothing.
 - `specialAttack()`: Empty class for subclasses.
 - `__str__()`: Adds all of the users stats up from their equipped items, and then sends a message with the structure:
 ```
 *********************
 {class name} Stats:
 Name: {name}
 Free Inventory Spaces: {free spaces}
 Hitpoints {hitpoints}
 Melee: {melee stat}
 Ranged: {ranged stat}
 Magic: {magic stat}
 Inventory: {list of items in inventory}
 Equipped Items: {list of equipped items}
 Melee Bonus: {melee bonus}
 Ranged Bonus: {ranged bonus}
 Mage Bonus: {mage bonus}
 Melee Defense: {melee defense}
 Ranged Defense: {ranged defense}
 Mage Defense: {mage defense}
 ```
## Project structure Superclasses
The project has a total of 5 subclasses
### Slot
A simple Enum class which contains `WEAPON`, `HELMET`, `CHEST`, `LEGS`, `BOOTS`, `CAPE`, and `NONE`
### Armour
Armour also includes Weapon for a reason I will never justify. The armour subclass contains 15 different functions:
 - `__init__(name: str, description: str, meleeBonus: int, rangedBonus: int, mageBonus: int, meleeDef: int, rangedDef: int, mageDef: int)`: Uses the parents `__init__()` function to define the name and description, then sets the remaining values to their respective variable.
 - `getMeleeBonus/getRangedBonus/getMageBonus/getMeleeDefense/getRangedDefense/getMageDefense()`: Gets the armour pieces respective stat.
 - `setMeleeBonus/setRangedBonus/setMageBonus/setMeleeDefense/setRangedDefense/setMageDefense(int)`: Sets the respective armour piece stat.
 - `getSlot()`: Returns the armour pieces `Slot`
 - `__str__`: Returns the armour stats with the following structure:
 ```
 {parents __str__}
 Slot: {slot}
 Melee Bonus: {melee bonus}
 Ranged Bonus: {ranged bonus}
 Magic Bonus: {magic bonus}
 Melee Defense: {melee defense}
 Ranged Defense: {ranged defense}
 Magic Defense: {magic defense}
 ```
### Tank
The tank is one of the character subclasses which defaults to 1000 HP, 30 melee, 1 ranged, and 1 magic. It has two functions:
 - `__init__(name: str, hitpoints: int, melee: int, ranged: int, mage: int)`: Initializes the character with the parents function.
 - `specialAttack()`: Gives the tank 500 extra HP, whilst boosting the melee stat by 10.
### Archer
Archer is another character subclass, starting with 100 HP, 1 melee, 99 ranged, and 1 magic. It also has two functions:
 - `__init__(name: str, hitpoints: int, melee: int, ranged: int, mage: int)`: Initializes the character with the parents function.
 - `specialAttack()`: Boosts the archers ranged by 13.
### Healer
The healer is the final character subclass, it defaults to 300 HP, 1 melee, 1 ranged, and 112 magic. The two functions are:
 - `__init__(name: str, hitpoints: int, melee: int, ranged: int, mage: int)`: Initializes the character with the parents function.
 - `specialAttack()`: Gives every other character in the `character` array (I told you it would be used later) by 250, while draining their own hitpoints to 50.
## Main Function
The main function simple creates some items to test, such as:
 - Creating a Wizard's Hat.
 - Creating a [Dinh's Bulwark](https://oldschool.runescape.wiki/w/Dinh%27s_bulwark).
 - Creating the Wisconsin Platebody.
 - Creating the [Infernal Cape](https://oldschool.runescape.wiki/w/Infernal_cape)
 - Creating a Healer named Joe.
 - Giving Joe a Wizard's Hat and Infernal Cape.
 - Equipping both items.
 - Creating a Tank Henry.
 - Giving Henry 5 Bulwarks and equipping one.
 - Giving Henry another two Bulwarks.
 - Trying to unequip a Bulwark with a full inventory
 - Dropping a Bulwark
 - Then sucessfully uneqipping the Bulwark
 - Printing Henry's Inventory
 - Creating an Archer Billy.
 - Giving Billy the Wisconsin Platebody
 - Printing Billy's Inventory
 - Printing Joe's character class.
 - Excecutuing Joe's special attack