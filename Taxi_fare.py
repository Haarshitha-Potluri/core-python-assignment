def calculate_fare(distances):
    fare = [(50 + 10 * distance) for distance in distances]
    total = sum(fare)
    return fare, total


trips = [5, 10, 3]
fares, total_fare = calculate_fare(trips)

for i, fare in enumerate(fares, 1):
    print(f"Trip {i}: ${fare}")
print(f"Total Fare: ${total_fare}")
