# taxi_fare Calculator

# Creating a fare calculator
def fare_calculator(distance_miles, base_fare, rate_per_meter):
    # Rate per meter remains the same
    # Convert miles to meters for calculation (1 mile = 1609.34 meters)
    total_fare = base_fare + (distance_miles * 1609.34 * rate_per_meter)
    return round(total_fare, 2)

#Input the base fare
base_fare = float(input("Enter the base fare amount: "))

# Input distance in miles
distance_miles = float(input("Enter the distance you have traveled (in Miles): "))

# Input the rate per meter
rate_per_meter = float(input("Enter the rate per meter (in dollars): "))


if distance_miles >= 0 and base_fare >= 0 and rate_per_meter >= 0:
    fare = fare_calculator(distance_miles, base_fare, rate_per_meter)
    print(f"The total cost of your trip should be {fare}")
else:
    print("Distance must be a non-negative number.")
