import sys

highestSale = 0
currentPaymentType = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:

        continue

    paymentType, saleAmount = data_mapped

    try:

        saleAmount = float(saleAmount)
    except ValueError:

        continue


    if currentPaymentType and currentPaymentType != paymentType:
        print(currentPaymentType + "\t" + str(highestSale))
        currentPaymentType = paymentType
        highestSale = 0

    currentPaymentType = paymentType
    if saleAmount > highestSale:
        highestSale = saleAmount


if currentPaymentType is not None:
    print(currentPaymentType + "\t" + str(highestSale))

