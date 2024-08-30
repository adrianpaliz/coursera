class PaySlips:
    def __init__(self, employee, payment, amount):
        self.employee = employee
        self.payment = payment
        self.amount = amount

    def pay(self):
        self.payment = 'yes'

    def status(self):
        if self.payment == 'yes':
            return self.employee + ' is paid ' + str(self.amount)
        else:
            return self.employee + ' is not paid yet'

nathan = PaySlips('Nathan', 'no', 1000)
roger = PaySlips('Roger', 'no', 1500)

print(nathan.status(), '\n', roger.status())

roger.pay()
print('After paymnet')
print(nathan.status(), '\n', roger.status())


