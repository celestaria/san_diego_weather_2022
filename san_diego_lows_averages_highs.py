# Import libraries and dependencies
from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Point, Daily

# Set time period
start = datetime(2022, 1, 1)
end = datetime(2022, 12, 31)

# Create point for San Diego, CA
san_diego = Point(32.7157, 117.1611, 62)

# Get daily data
data = Daily(san_diego, start, end)
data = data.fetch()

# Plot line chart showing minimum, average, and maximum temperature
ax = data.plot(
    y=['tavg', 'tmin', 'tmax'],
    lw=2,
    colormap='jet',
    marker='.',
    markersize=10,
    figsize=(10, 7.5)
    )
ax.set_title("Daily average, low, and high temperatures - 2022 San Diego, CA", fontsize=20)
ax.set_xlabel("Dates", fontsize =16)
ax.set_ylabel("Temperature (C)", fontsize =16)
plt.show()
