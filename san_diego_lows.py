# Import libraries and dependencies
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from meteostat import Point, Daily

# Set time period
start = datetime(2022, 1, 1)
end = datetime(2022, 12, 29)

# Create point for San Diego, CA
san_diego = Point(32.7157, 117.1611, 62)

# Get daily data
data = Daily(san_diego, start, end)
data = data.fetch()

# Create x and y values for minimum temperature
x = mdates.date2num(data.tmin.index)
y = data.tmin.values

# Calculate equation for trendline for minium temperature
z = np.polyfit(x, y, 1)
p = np.poly1d(z)

# Add trendline to plot for minimum temperature
plt.style.use('seaborn')
title = "Daily low temperatures - 2022 San Diego, CA"
fig, ax = plt.subplots()
ax.set_title(title, fontsize=20)
ax.set_xlabel('Dates', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (C)", fontsize=16)
plt.scatter(data.tmin.index, y)
plt.plot(x, p(x))

plt.show()