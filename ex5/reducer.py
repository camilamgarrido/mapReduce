import sys


totalSales = 0


for line in sys.stdin:
    data_mapped = line.strip().split("\t")


    if len(data_mapped) != 2:
        continue

    key, saleAmount = data_mapped

    try:
        saleAmount = float(saleAmount)
    except ValueError:
        continue


    if key == "total":
        totalSales += saleAmount


print("Total Sales: " + str(totalSales))

