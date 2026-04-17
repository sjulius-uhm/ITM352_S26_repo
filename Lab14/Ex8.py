# Create a heatmap from pickup and dropoff community areas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

trips_df = pd.read_csv('../taxi trips Fri 7_7_2017.csv')

trips_df = trips_df[['pickup_community_area', 'dropoff_community_area']]
trips_df = trips_df.dropna()
pickup_area = trips_df.pickup_community_area
dropoff_area = trips_df.dropoff_community_area

fig = plt.figure()

area_table = pd.crosstab(pickup_area, dropoff_area)

sns.heatmap(area_table)

plt.title('Taxi Trips Heatmap (Pickup vs Dropoff Areas)')
plt.xlabel('Dropoff Community Area')
plt.ylabel('Pickup Community Area')

plt.show()