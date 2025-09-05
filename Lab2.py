# Function 1: Calculate the height of the ball after time t
# This function should take the initial height h0 and time t as inputs, and return the height at time t.
# Round up to one decimal point
def calculate_height(h0, t):
    g = 9.8
    height = h0 - 0.5 * g * t**2
    return round(height, 1)

    def main():
        h0 = float(input("Enter initial height: "))
        t = float(input("Enter time: "))
        height = calculate_height(h0, t)
        print(f"Height of the ball at time {t} second = {height} meters")
        

# Function 2: Calculate the distance traveled by the car
# This function should take the time t as input and return the distance traveled by the car.
def calculate_car_distance(t):
    # TODO: Implement this function
    pass  # Replace with your code
    def calculate_car_distance(t):
        speed = 20
        distance = speed * t
        return distance
