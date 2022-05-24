from collections import Counter

flower_orders = ['W/R/B', 'W/R/B', 'W/R/B', 'W/R/B', 'W/R/B', 'W/R/B', 'W/R/B', 'W/R/B', 'W/R/B', 'W/R/B', 'W/R/B',
                 'W/R/B', 'W/R/B', 'W/R/B', 'W/R/B', 'W/R/B', 'W/R/B', 'W/R/B', 'W/R/B', 'W/R/B', 'W/R/B', 'W/R/B',
                 'W/R/B', 'W/R/B', 'W/R/B', 'W/R/B', 'W/R/B', 'W/R/B', 'W/R/B', 'W/R/B', 'W/R', 'W/R', 'W/R', 'W/R',
                 'W/R', 'W/R', 'W/R', 'W/R', 'W/R', 'W/R', 'W/R', 'W/R', 'W/R', 'W/R', 'W/R', 'W/R', 'R/V/Y', 'R/V/Y',
                 'R/V/Y', 'R/V/Y', 'R/V/Y', 'R/V/Y', 'R/V/Y', 'R/V/Y', 'R/V/Y', 'R/V/Y', 'W/R/V', 'W/R/V', 'W/R/V',
                 'W/R/V', 'W/R/V', 'W/R/V', 'W/R/V', 'W/R/V', 'W/R/V', 'W/R/V', 'W/N/R/V', 'W/N/R/V', 'W/N/R/V',
                 'W/N/R/V', 'W/N/R/V', 'W/N/R/V', 'W/N/R/V', 'W/N/R/V', 'W/R/B/Y', 'W/R/B/Y', 'W/R/B/Y', 'W/R/B/Y',
                 'W/R/B/Y', 'W/R/B/Y', 'B/Y', 'B/Y', 'B/Y', 'B/Y', 'B/Y', 'R/B/Y', 'R/B/Y', 'R/B/Y', 'R/B/Y', 'R/B/Y',
                 'W/N/R/B/V/Y', 'W/N/R/B/V/Y', 'W/N/R/B/V/Y', 'W/N/R/B/V/Y', 'W/N/R/B/V/Y', 'W/G', 'W/G', 'W/G', 'W/G',
                 'R/Y', 'R/Y', 'R/Y', 'R/Y', 'N/R/V/Y', 'N/R/V/Y', 'N/R/V/Y', 'N/R/V/Y', 'W/R/B/V', 'W/R/B/V',
                 'W/R/B/V', 'W/R/B/V', 'W/N/R/V/Y', 'W/N/R/V/Y', 'W/N/R/V/Y', 'W/N/R/V/Y', 'N/R/Y', 'N/R/Y', 'N/R/Y',
                 'W/V/O', 'W/V/O', 'W/V/O', 'W/N/R/Y', 'W/N/R/Y', 'W/N/R/Y', 'R/B/V/Y', 'R/B/V/Y', 'R/B/V/Y', 'W/R/V/Y',
                 'W/R/V/Y', 'W/R/V/Y', 'W/R/B/V/Y', 'W/R/B/V/Y', 'W/R/B/V/Y', 'W/N/R/B/Y', 'W/N/R/B/Y', 'W/N/R/B/Y',
                 'R/G', 'R/G', 'B/V/Y', 'B/V/Y', 'N/B/Y', 'N/B/Y', 'W/B/Y', 'W/B/Y', 'W/N/B', 'W/N/B', 'W/N/R', 'W/N/R',
                 'W/N/B/Y', 'W/N/B/Y', 'W/B/V/Y', 'W/B/V/Y', 'W/N/R/B/V/Y/G/M', 'W/N/R/B/V/Y/G/M', 'B/R', 'N/R', 'V/Y',
                 'V', 'N/R/V', 'N/V/Y', 'R/B/O', 'W/B/V', 'W/V/Y', 'W/N/R/B', 'W/N/R/O', 'W/N/R/G', 'W/N/V/Y',
                 'W/N/Y/M', 'N/R/B/Y', 'N/B/V/Y', 'R/V/Y/O', 'W/B/V/M', 'W/B/V/O', 'N/R/B/Y/M', 'N/R/V/O/M',
                 'W/N/R/Y/G', 'N/R/B/V/Y', 'W/R/B/V/Y/P', 'W/N/R/B/Y/G', 'W/N/R/B/V/O/M', 'W/N/R/B/V/Y/M',
                 'W/N/B/V/Y/G/M', 'W/N/B/V/V/Y/P']
print(flower_orders)

flower_orders_updated = []

for i in flower_orders:
    j = i.replace("/", "")
    flower_orders_updated.append(j)

print(flower_orders_updated)

count = 0
for i in flower_orders_updated:
    if i.__contains__('W'):
        count = count + 1
        print(i)

# printing result
print("Count of W: " + str(count))

StringFlowerOrder = "".join(flower_orders_updated)
print(StringFlowerOrder)

from collections import Counter

dictflowers = dict(Counter(StringFlowerOrder))
print(dictflowers)

import matplotlib.pyplot as plt
plt.bar(dictflowers.keys(), dictflowers.values())
plt.show()