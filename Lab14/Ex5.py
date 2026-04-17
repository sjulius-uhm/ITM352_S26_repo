# Create a scatterplot of fare by trip miles.  Save the plot to a PNG file. 
import pandas as pd
import matplotlib.pyplot as plt

trips_df = pd.read_json('../Trips from area 8.json')

trip_miles_gt_0 = trips_df[['trip_miles', 'fare']].query('trip_miles > 0')
fare_series = trip_miles_gt_0.fare
trip_miles = trip_miles_gt_0.trip_miles

fig = plt.figure()

# Use a cyan colored triangle down marker with a transparency of 0.2
plt.plot(trip_miles, fare_series, linestyle= "none", marker=".")
plt.plot(trip_miles, fare_series, marker = "v", linestyle = "none", color = 'c', label = "Taxi Fare", alpha = 0.2)
plt.scatter(trip_miles, fare_series)
plt.title('Fares by Taxi Trip Miles')
plt.xlabel('Miles')
plt.ylabel('Dollars')
plt.legend()
plt.show()