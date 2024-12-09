import sys

salesTotal = 0
oldCategory = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:

        continue

    thisCategory, thisSale = data_mapped

    try:
        thisSale = float(thisSale)
    except ValueError:
  
        continue


    if oldCategory and oldCategory != thisCategory:
        print(oldCategory + "\t" + str(salesTotal))
        oldCategory = thisCategory
        salesTotal = 0

    oldCategory = thisCategory
    salesTotal += thisSale


if oldCategory is not None:
    print(oldCategory + "\t" + str(salesTotal))

