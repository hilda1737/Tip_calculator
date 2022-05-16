print("welcome to tip calculator?")
bill=float(input("what is the bill?"))
tip=int(input("what tip would you like to give? 10 12 15"))
bill_with_tip= tip/100 * bill + bill
print(bill_with_tip)