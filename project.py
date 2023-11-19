#im sorry this file the same thing over and over and over and over again

from enum import Enum

class ArmourSlot(Enum):
    WEAPON = "Weapon"
    HELMET = "Helmet"
    CHEST = "Chestpiece"
    LEGS = "Platelegs"
    BOOTS = "Boots"
    CAPE = "Cape"
    NONE = "Armour Piece"

class Item:
    def __init__(self, name = "Default Item Name", description = "No Description."):
        self.__name = name
        self.__description = description

    def getName(self):
        return self.__name
    
    def getDescription(self):
        return self.__description
    
    def getClass(self):
        return self.__class
    
    def __str__(self):
        return f"{type(self).__name__} Stats:\nName: {self.getName()}\nDescription: {self.__description}"
    
class Armour(Item):
    def __init__(self, name = "Unnamed Armour Piece", description = "No Description.", meleeBonus = 0, rangedBonus = 0, mageBonus = 0, meleeDef = 0, rangedDef = 0, mageDef = 0, slot = ArmourSlot.NONE):
        super().__init__(name, description)
        self.__meleeBonus = meleeBonus
        self.__rangedBonus = rangedBonus
        self.__mageBonus = mageBonus
        self.__meleeDef = meleeDef
        self.__rangedDef = rangedDef
        self.__mageDef = mageDef
        self.__slot = slot

    def getMeleeBonus(self):
        return self.__meleeBonus
    
    def getRangedBonus(self):
        return self.__rangedBonus
    
    def getMageBonus(self):
        return self.__mageBonus
    
    def setMeleeBonus(self, bonus):
        self.__meleeBonus = bonus

    def setRangedBonus(self, bonus):
        self.__rangedBonus = bonus

    def setMageBonus(self, bonus):
        self.__mageBonus = bonus

    def getMeleeDefense(self):
        return self.__meleeDef
    
    def getRangedDefense(self):
        return self.__rangedDef
    
    def getMageDefense(self):
        return self.__mageDef
    
    def setMeleeDefense(self, defense):
        self.__meleeDef = defense

    def setRangedDefense(self, defense):
        self.__rangedDef = defense

    def setMageDefense(self, defense):
        self.__mageDef = defense

    def getSlot(self):
        return self.__slot

    def __str__(self):
        return f"{super().__str__()}\nSlot: {self.__slot.value}\nMelee Bonus: {self.__meleeBonus}\nRanged Bonus: {self.__rangedBonus}\nMage Bonus: {self.__mageBonus}\nMelee Defense: {self.__meleeDef}\nRanged Defense: {self.__rangedDef}\nMage Defense: {self.__mageDef}"
    
characters = []

class Character:
    def __init__(self, name = "Jimmy", hitpoints = 10, melee = 1, ranged = 1, magic = 1):
        characters.append(self)
        self.__name = name
        self.__hitpoints = hitpoints
        self.__melee = melee
        self.__ranged = ranged
        self.__magic = magic
        self.__inventory = [None, None, None, None, None]
        self.__armour = {
            "Weapon": None,
            "Helmet": None,
            "Chestpiece": None,
            "Platelegs": None,
            "Boots": None,
            "Cape": None
        }

    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name

    def getHitpoints(self):
        return self.__hitpoints
    
    def removeHitpoints(self, amount):
        print(f"{self.__name} lost {amount} HP!")
        self.__hitpoints -= amount
        if self.__hitpoints <= 0:
            print(f"Oh dear, {self.__name} has died!") #shoutout runescape
    
    def addHitpoints(self, amount):
        print(f"{self.__name} gained {amount} hitpoints!")
        self.__hitpoints += amount
    
    def getMelee(self):
        return self.__melee

    def getRanged(self):
        return self.__ranged
    
    def getMagic(self):
        return self.__magic
    
    def boostMelee(self, amount):
        self.__melee += amount
        print(f"{self.__name} had their melee stats boosted by {amount} to {self.__melee}!")

    def boostRanged(self, amount):
        self.__ranged += amount
        print(f"{self.__name} had their ranged stats boosted by {amount} to {self.__ranged}!")

    def boostMagic(self, amount):
        self.__magic += amount
        print(f"{self.__name} had their magic stats boosted by {amount} to {self.__magic}!")

    def drainMelee(self, amount):
        self.__melee -= amount
        print(f"{self.__name} had their melee stats drained by {amount} to {self.__melee}!")

    def drainRanged(self, amount):
        self.__ranged -= amount
        print(f"{self.__name} had their ranged stats drained by {amount} to {self.__ranged}!")

    def drainMagic(self, amount):
        self.__magic -= amount
        print(f"{self.__name} had their magic stats drained by {amount} to {self.__magic}!")

    def getInventory(self):
        items = f"{self.__name}'s Inventory: "
        for item in self.__inventory:
            if item != None:
                items += item.getName() + ", "
        return items[:-2]
    
    def addItem(self, item):
        if self.__inventory.count(None) > 0:
            self.__inventory[self.__inventory.index(None)] = item
            print(f"{self.__name} has added {item.getName()} to their backpack!")
        else:
            print(f"{self.__name} has no room in their backpack!")

    def dropItem(self, itemName):
        i = 0
        for item in self.__inventory:
            if item != None and item.getName() == itemName:
                self.__inventory[i] = None
                print(f"{self.__name} has dropped {itemName}! They have {self.__inventory.count(None)} inventory spaces remaining")
                return
            i+=1
        print("No item with that name found!")

    def getItems(self):
        armour = ""
        for slot in self.__armour:
            if self.__armour[slot] != None:
                armour += f"{slot} - {self.__armour[slot].getName()}\n"
            else:
                armour += f"{slot} - Empty\n"
        return armour[:-1]

    def equipItem(self, armour):
        i = 0
        for slot in self.__inventory:
            if slot != None and self.__inventory[i].getName() == armour.getName():
                item = self.__inventory[i]
                if self.__armour[item.getSlot().value] != None:
                    print(f"Please unequip {self.__armour[item.getSlot().value].getName()} before equiping this item!")
                    return
                else:
                    self.__armour[item.getSlot().value] = item
                    self.__inventory[self.__inventory.index(slot)] = None
                    return
            i+=1
        print("Item could not be found!")

    def unequipItem(self, armourName):
        if self.__inventory.count(None) <= 0:
            print(f"{self.__name} has no free inventory space! Please drop an item.")
            return
        i = 0
        for slot in self.__armour:
            if self.__armour[slot] != None and self.__armour[slot].getName() == armourName:
                self.__inventory[self.__inventory.index(None)] = self.__armour[slot]
                self.__armour[slot] = None
                print(f"{self.__name} has put {armourName} in their inventory! They have {self.__inventory.count(None)} inventory spaces remaining")
                return
            i+=1
        print("No item with that name found!")
        i+=1

    def specialAttack(self):
        pass

    def __str__(self):
        meleeDef = 0
        rangedDef = 0
        mageDef = 0
        meleeBonus = 0
        rangedBonus = 0
        mageBonus = 0
        for slot in self.__armour:
            if self.__armour[slot] != None:
                armour = self.__armour[slot]
                meleeDef += armour.getMeleeDefense()
                mageDef += armour.getMageDefense()
                rangedDef += armour.getRangedDefense()
                meleeBonus += armour.getMeleeBonus()
                rangedBonus += armour.getRangedBonus()
                mageBonus += armour.getMageBonus()
        return f"*********************\n{type(self).__name__} Stats:\nName: {self.__name}\nFree Inventory Spaces: {self.__inventory.count(None)}\nHitpoints: {self.__hitpoints}\nMelee: {self.__melee}\nRanged: {self.__ranged}\nMagic: {self.__magic}\nInventory: {self.getInventory()}\nEquipped Items: \n{self.getItems()}\nMelee Bonus: {meleeBonus}\nRanged Bonus: {rangedBonus}\nMage Bonus: {mageBonus}\nMelee Defense: {meleeDef}\nRanged Defense: {rangedDef}\nMage Defense: {mageDef}"

class Tank(Character):
    def __init__(self, name = "Tank", hitpoints = 1000, melee = 30, ranged = 1, magic = 1):
        super().__init__(name, hitpoints, melee, ranged, magic)

    def specialAttack(self):
        print(f"{self.getName()} uses all of their power to boost their hitpoints and melee stats!")
        self.addHitpoints(500)
        self.boostMelee(10)

class Archer(Character):
    def __init__(self, name = "Archer", hitpoints = 100, melee = 1, ranged = 99, magic = 1):
        super().__init__(name, hitpoints, melee, ranged, magic)

    def specialAttack(self):
        print(f"{self.getName()} Focusses on their attacks!")
        self.boostRanged(12)

class Healer(Character):
    def __init__(self, name = "Healer", hitpoints = 300, melee = 30, ranged = 1, magic = 1):
        super().__init__(name, hitpoints, melee, ranged, magic)

    def specialAttack(self):
        print(f"{self.getName()} Uses their hitpoints to heal the team!!")
        self.removeHitpoints(self.getHitpoints()-50)
        for character in characters:
            if character != self:
                character.addHitpoints(250)

def main():
    #test code
    wizardsHat = Armour("Wizard's Hat", "A magical hat rumoured to boost magical spells", mageBonus=30, slot=ArmourSlot.HELMET)
    dinhsBulwark = Armour("Dinh's Bulwark", "A two-handed shield created by Dinh", meleeDef=300, rangedDef=400, slot=ArmourSlot.WEAPON)
    wisconsinPlatebody = Armour("Wisconsin Platebody", "Armour once worn by a powerful ranger", rangedBonus=100, slot=ArmourSlot.CHEST)
    infernalCape = Armour("Infernal Cape", "A cape awarded to the most talented of warriors", meleeBonus=10, slot=ArmourSlot.CAPE)
    joe = Healer("Joe")
    joe.addItem(wizardsHat)
    joe.addItem(infernalCape)
    joe.equipItem(wizardsHat)
    joe.equipItem(infernalCape)
    henry = Tank("Henry")
    henry.addItem(dinhsBulwark)
    henry.addItem(dinhsBulwark)
    henry.addItem(dinhsBulwark)
    henry.addItem(dinhsBulwark)
    henry.addItem(dinhsBulwark)
    henry.equipItem(dinhsBulwark)
    henry.addItem(dinhsBulwark)
    henry.addItem(dinhsBulwark)
    henry.unequipItem("Dinh's Bulwark")
    henry.dropItem("Dinh's Bulwark")
    henry.unequipItem("Dinh's Bulwark")
    print(henry.getInventory())
    billy = Archer("Billy")
    billy.addItem(wisconsinPlatebody)
    print(billy.getInventory())
    print(joe)
    joe.specialAttack()

if __name__ == "__main__":
    main()