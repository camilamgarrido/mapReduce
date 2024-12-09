import sys


highestSale = 0


for line in sys.stdin:
    data_mapped = line.strip().split("\t")


    if len(data_mapped) != 2:
        continue

    paymentType, saleAmount = data_mapped


    try:
        saleAmount = float(saleAmount)
    except ValueError:
        continue


    if saleAmount > highestSale:
        highestSale = saleAmount


print("Maximum Sale Amount: " + str(highestSale))

