# Import libraries and dependencies
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
from meteostat import Point, Daily

# Set time period
start = datetime(2022, 1, 1)
end = datetime(2022, 12, 29)

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
    title='Daily average, low, and high temperatures - 2022 San Diego, CA'
    )
ax.set_xlabel("Dates")
ax.set_ylabel("Temperature (C)")
plt.show()