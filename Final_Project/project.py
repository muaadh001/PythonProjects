import requests

def fetch_weather_data(location, start_date, end_date):
    
    data = [
        {"date": "2023-06-01", "temp": 20},
        {"date": "2023-06-02", "temp": 22},
        {"date": "2023-06-03", "temp": 21},
        {"date": "2023-06-04", "temp": 23},
        {"date": "2023-06-05", "temp": 19}
    ]
    return data

def process_weather_data(data):
    temperatures = [day["temp"] for day in data]
    avg_temp = sum(temperatures) / len(temperatures)
    max_temp = max(temperatures)
    min_temp = min(temperatures)
    return {
        "average": avg_temp,
        "highest": max_temp,
        "lowest": min_temp
    }

def display_weather_summary(location, start_date, end_date, summary):
    print(f"Weather summary for {location} from {start_date} to {end_date}:")
    print(f"Average Temperature: {summary['average']}°C")
    print(f"Highest Temperature: {summary['highest']}°C")
    print(f"Lowest Temperature: {summary['lowest']}°C")

def main():
    location = input("Enter location: ")
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")

    data = fetch_weather_data(location, start_date, end_date)
    summary = process_weather_data(data)
    display_weather_summary(location, start_date, end_date, summary)

if __name__ == "__main__":
    main()
