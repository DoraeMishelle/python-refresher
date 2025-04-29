from user import StringName

# simply print a line to ensure everything is functional
print ("bool")

#class refresher
#create a class and function
class ObedientCharacter:
    def __init__(self, height, speed, strength):
        self.heigh = height
        self.speed = speed
        self.strength = strength

#learning design patterns
        
#start with classes
class NewString():
    def __init__(self):
        self.s2 = StringName()

    def newName(self,newName):
        self.s2.userName(newName)
        
newstring = NewString()
newstring.newName("Mishelle")