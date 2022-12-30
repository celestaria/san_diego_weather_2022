# Import libraries and dependencies
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from scipy.stats.stats import pearsonr
from meteostat import Point, Daily

# Set time period
start = datetime(2022, 1, 1)
end = datetime(2022, 12, 29)

# Create point for San Diego, CA
san_diego = Point(32.7157, 117.1611, 62)

# Get daily data
data = Daily(san_diego, start, end)
data = data.fetch()

# Create x and y values for pressure
x = data.pres
y = data.tavg

# Calculate equation for trendline for pressure
z = np.polyfit(x, y, 1)
p = np.poly1d(z)

# Plot average precipitation
plt.style.use('seaborn')
title = "Daily Pressure vs Average Temperature- 2022 San Diego, CA"
fig, ax = plt.subplots()
ax.set_title(title, fontsize=20)
ax.set_xlabel('Pressure (hPa)', fontsize=16)
ax.set_ylabel("Temperature (C)", fontsize=16)
plt.scatter(x, y)
plt.plot(x, p(x))
plt.show()

print(np.corrcoef(x, y)[0,1])
print(pearsonr(x, y))