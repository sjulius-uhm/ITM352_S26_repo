import pandas as pd
import matplotlib.pyplot as plt

# Load data
trips_df = pd.read_json('../Trips from area 8.json')

# Keep only needed columns and convert to numeric
trips_df = trips_df[['trip_miles', 'fare']]
trips_df['trip_miles'] = pd.to_numeric(trips_df['trip_miles'], errors='coerce')
trips_df['fare'] = pd.to_numeric(trips_df['fare'], errors='coerce')

# Drop NA values
trips_df = trips_df.dropna()

# b + c: Filter out trips of 0 miles and less than 2 miles
filtered_df = trips_df[trips_df['trip_miles'] >= 2]

# Create scatter plot (fare on X, miles on Y)
plt.scatter(filtered_df['fare'], filtered_df['trip_miles'])

# Labels and title
plt.xlabel('Fare ($)')
plt.ylabel('Trip Miles')
plt.title('Trip Miles by Fare (Trips ≥ 2 miles)')

# a: Save the plot
plt.savefig('FaresXmiles.png', dpi=300)

plt.show()