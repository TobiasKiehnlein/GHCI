import csv
import time

import matplotlib.patches as patches
import matplotlib.pyplot as plt

from utils import get_euclidean_distance

with open('eyedata.csv', newline='\n') as csv_file:
    x, y = map(list, zip(*[[int(x[0]), int(x[1])] for x in csv.reader(csv_file, delimiter=';')]))

for i in range(1, len(x)):
    if get_euclidean_distance([x[i], y[i]], [x[i - 1], y[i - 1]]) > 20:
        millis = int(i / 60 * 1000)
        print(f'{str(millis // 1000 // 60).rjust(2, "0")}:{str((millis // 1000) % 60).rjust(2, "0")}:{str(millis % 1000).rjust(3, "0")}')

fig, ax = plt.subplots()
plt.hexbin(x, y, bins='log', cmap='magma', gridsize=200)
plt.axis([min(x), max(x), min(y), max(y)])
plt.gcf().set_dpi(300)

rect = patches.Rectangle((0, 0), 1280, 800, linewidth=1, edgecolor='w', facecolor='none')
ax.add_patch(rect)

cb = plt.colorbar()
plt.show()
