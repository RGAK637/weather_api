import requests

def get_weather_data():
    URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
    try:
        response = requests.get(URL)
        db = response.json()
        return db
    except requests.RequestException:
        print("Failed to fetch data from the API.")
        return None

def get_temperature(data, date):
    for forecast in data["list"]:
        if forecast["dt_txt"].startswith(date):
            return forecast["main"]["temp"]

    print("Date not found in the forecast.")
    return None

def get_wind_speed(data, date):
    for forecast in data["list"]:
        if forecast["dt_txt"].startswith(date):
            return forecast["wind"]["speed"]

    print("Date not found in the forecast.")
    return None

def get_pressure(data, date):
    for forecast in data["list"]:
        if forecast["dt_txt"].startswith(date):
            return forecast["main"]["pressure"]

    print("Date not found in the forecast.")
    return None

def main():
    db = get_weather_data()

    if db:
        while True:
            print("\nOptions:")
            print("1. Get temperature")
            print("2. Get wind speed")
            print("3. Get pressure")
            print("0. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                date = input("Enter the date (YYYY-MM-DD): ")
                temperature = get_temperature(db, date)
                if temperature is not None:
                    print(f"Temperature on {date}: {temperature} °C")

            elif choice == "2":
                date = input("Enter the date (YYYY-MM-DD): ")
                wind_speed = get_wind_speed(db, date)
                if wind_speed is not None:
                    print(f"Wind Speed on {date}: {wind_speed} m/s")

            elif choice == "3":
                date = input("Enter the date (YYYY-MM-DD): ")
                pressure = get_pressure(db, date)
                if pressure is not None:
                    print(f"Pressure on {date}: {pressure} hPa")

            elif choice == "0":
                print("Exiting the program.")
                break

            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
