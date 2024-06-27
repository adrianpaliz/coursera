#print('Hello')

#The next line will give a error
#print('hello') print('world')
#Solving this error moving the second print satatement to a new line
'''
print('Hello')
print('world')
'''
#Solving adding a semicolon in the same line
#print('Hello'); print('world')

#The impact of white spaces
'''
my_variable = 1 +     2 #Extra white spaces don't cause problems
print(my_variable)
'''
#Adding a new line
'''
my_variable = 2 + 3
+ 4 #The interpreter don't execute this new line
print(my_variable)
'''
#Solving using force line typing a backslash \
'''
my_variable = 2 + 3 \
+ 4
print(my_variable)
'''

#Indentation
name = 'Adrián'
if name == 'Adrián':
    print(name) #If I delete indentation a get IndentationError

