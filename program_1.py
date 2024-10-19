def get_rainfall_data():
    rainfall = []
    for i in range(1,13):
        while True:
            try:
                rain = float(input(f"Enter the total rainfall for month {i}: "))
                if rain < 0:
                    print("Rainfall cannot be negative. Please enter a valid number.")
                else:
                    rainfall.append(rain)
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    return rainfall

def calculate_total(rainfall):
    return sum(rainfall)

def calculate_average(rainfall):
    return sum(rainfall) / len(rainfall)

def find_extremes(rainfall):
    max_rain = max(rainfall)
    min_rain = min(rainfall)
    max_month = rainfall.index(max_rain) + 1  
    min_month = rainfall.index(min_rain) + 1
    return max_month, max_rain, min_month, min_rain

def main():
    rainfall = get_rainfall_data()
    total_rainfall = calculate_total(rainfall)
    average_rainfall = calculate_average(rainfall)
    max_month, max_rain, min_month, min_rain = find_extremes(rainfall)

    print("\nRainfall Statistics:")
    print(f"Total rainfall for the year: {total_rainfall:.2f} inches")
    print(f"Average monthly rainfall: {average_rainfall:.2f} inches")
    print(f"Month {max_month} had the highest rainfall: {max_rain:.2f} inches")
    print(f"Month {min_month} had the lowest rainfall: {min_rain:.2f} inches")

if __name__ == "__main__":
    main()
    