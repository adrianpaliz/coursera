class Keyboard:
    def language(self):
        return 'Function inside Keyboard'

class Screen:
    def language(self):
        return 'Function inside Screen'

class Laptop:
    def language(self):
        return 'Function inside Laptop'
    
class Workstation(Keyboard, Screen):
    def language(self):
        return 'Function inside Workstation'

class Desktop(Screen, Laptop):
    def language(self):
        return 'Function inside Desktop'

class Office(Desktop, Workstation, Laptop):
    pass

office = Office()
print(office.language())
print(Office.mro())

