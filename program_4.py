import math

# Function to calculate distance between two 3D points
def distance(point1, point2):
    # Unpack the coordinates from the tuples
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    
    # Apply the distance formula
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    return dist

# Function to get a valid 3D coordinate tuple from the user
def get_coordinate_input(point_number):
    while True:
        try:
            # Prompt the user for x, y, z values
            x = float(input(f"Enter the x-coordinate for point {point_number}: "))
            y = float(input(f"Enter the y-coordinate for point {point_number}: "))
            z = float(input(f"Enter the z-coordinate for point {point_number}: "))
            
            # Return the coordinates as a tuple
            return (x, y, z)
        except ValueError:
            print("Invalid input. Please enter numeric values for the coordinates.")

# Mainline program
def main():
    print("This program calculates the distance between two points in 3D space.")

    # Get the two 3D coordinates from the user
    point1 = get_coordinate_input(1)
    point2 = get_coordinate_input(2)

    # Call the distance function to calculate the distance
    dist = distance(point1, point2)

    # Display the calculated distance
    print(f"\nThe distance between {point1} and {point2} is: {dist:.2f}")

# Run the program
if __name__ == "__main__":
    main()