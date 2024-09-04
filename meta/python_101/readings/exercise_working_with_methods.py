class Terminal:
    def version(self):
        return 'Function inside Terminal'

class Gnome:
    pass

class Firefox:
    def version(self):
        return 'Function inside Firefox'

class Ubuntu(Gnome, Firefox, Terminal):
    pass

class Ubuntu(Firefox):
    pass

ubuntu = Ubuntu()
print(ubuntu.version())

