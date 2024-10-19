#I wanted to start over because I wasn't getting the code right.

def get_state_data():
    data = []
    
    while True:
        try:
            # Get year input
            year = int(input("Enter the year (or -1 to stop): "))
            if year == -1:
                break

            # Get state name input
            state = input("Enter the name of the state: ")

            # Get population input
            population = int(input("Enter the population: "))

            # Append the data as a list
            data.append([year, state, population])
        except ValueError:
            print("Invalid input. Please enter numeric values for year and population.")
    
    return data

# Function to calculate total population for a specific year
def calculate_population_for_year(data, target_year):
    total_population = 0
    for record in data:
        year, state, population = record
        if year == target_year:
            total_population += population
    return total_population

# Main program logic
def main():
    # Get state data from the user
    state_data = get_state_data()

    if not state_data:
        print("No data was entered.")
        return

    # Get the target year from the user
    try:
        target_year = int(input("Enter the year to calculate total population: "))
    except ValueError:
        print("Invalid year input.")
        return

    # Calculate total population for the specified year
    total_population = calculate_population_for_year(state_data, target_year)

    # Display the result
    if total_population == 0:
        print(f"No data found for the year {target_year}.")
    else:
        print(f"Total population for the year {target_year}: {total_population}")

# Run the program
if __name__ == "__main__":
    main()