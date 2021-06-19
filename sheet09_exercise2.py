import csv
import math

import matplotlib.patches as patches
import matplotlib.pyplot as plt


def get_euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


with open('eyedata.csv', newline='\n') as csvfile:
    data = [[int(y) for y in x] for x in csv.reader(csvfile, delimiter=';')]

for i in range(1, len(data)):
    if get_euclidean_distance(data[i], data[i - 1]) > 20:
        millis = int(i / 60 * 1000)
        print(f'{str(millis // 1000 // 60).rjust(2, "0")}:{str((millis // 1000) % 60).rjust(2, "0")}:{str(millis % 1000).rjust(3, "0")}')

x = [elt[0] for elt in data]
y = [elt[1] for elt in data]

fig, ax = plt.subplots()
plt.hexbin(x, y, bins='log')
plt.axis([min(x), max(x), min(y), max(y)])

rect = patches.Rectangle((0, 0), 1280, 800, linewidth=1, edgecolor='w', facecolor='none')
ax.add_patch(rect)

cb = plt.colorbar()
plt.show()
