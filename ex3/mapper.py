import sys
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 6:
        continue
    date, time, store, category, cost, payment = data
    try:
        cost = float(cost)
    except ValueError:
        continue
    print(payment + "\t" + str(cost))
