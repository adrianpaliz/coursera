loyalty_customer = True
total_bill = 124

if loyalty_customer and total_bill > 100:
    # Give 20% discount
    total_bill = total_bill - (float(total_bill) / 100) * 20
elif total_bill > 100:
    # Give 10% discount
    total_bill = total_bill - (float(total_bill) / 100) * 10
else:
    # Sorry no discount, 5% service charge applied.
    print('Sorry, no discount...')

print('Total Bill: ', float(total_bill))

