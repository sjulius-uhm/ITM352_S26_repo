# Calculate stats ONLY for fares greater than $10

import csv

filename = "taxi_1000.csv"
with open(filename) as csvfile:
    csv_reader = csv.reader(csvfile)

    total_fare = 0.0
    max_distance = 0.0
    num_rows = 0
    valid_rows = 0

    for line in csv_reader:
        if num_rows == 0:
            fare_index = line.index("Fare")
            distance_index = line.index("Trip Miles")
            num_rows += 1
            continue

        tripFare = float(line[fare_index])
        tripDistance = float(line[distance_index])

        if tripFare > 10: 
            total_fare += tripFare
            valid_rows += 1

            if tripDistance > max_distance:
                max_distance = tripDistance

        num_rows += 1

    if valid_rows > 0:
        average_fare = total_fare / valid_rows
    else:
        average_fare = 0

    print(f"Rows with fare > $10: {valid_rows}")
    print(f"Total fare: ${total_fare:.2f}")
    print(f"Average fare: ${average_fare:.2f}")
    print(f"Max trip distance: {max_distance}")