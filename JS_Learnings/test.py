import sys
MAX_INT = sys.maxsize
n = 4

def calculateBill(units: int) -> int:

    bill = 0

    charges = [1.5, 2.5, 4.0]
    range_ = [100, 200, MAX_INT]

    for i in range(n):
        if units <= range_[i]:
            bill += charges[i] * units
            break
        else:
            bill += charges[i] * range_[i]
            units -= range_[i]
    return bill

print("Electricity Bill Calculator".center(70, '-'))
units = int(input("Please enter number of units used for the month: "))
bill = calculateBill(units)
print(f"Bill for the current month: {bill:.1f}")
