# Control flow
'''
The order in wich the instructions in a program are executed.
'''

# Python has two types of control flows
# Conditional statemens
'''
if
else
elif (else if)
'''
# Loops
'''
for loop
while loop
'''

bill_total = 210
discount_1 = 10
discount_2 = 20

if bill_total > 100 and bill_total < 200:
    print('Bill is greater than 100!')
    bill_total = bill_total - discount_1
elif bill_total > 200:
    print('Bill is greater than 200!')
    bill_total = bill_total - discount_2
else:
    print('Bill is less than 100!')

print('Total bill: ' + str(bill_total))

