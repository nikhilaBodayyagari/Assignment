import requests

def get_weather_data(location):
    api_key = "b6907d289e10d714a6e88b30761fae22"
    url = f"https://samples.openweathermap.org/data/2.5/forecast/hourly?q={location}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error: Failed to fetch data from the API.")
        return None

def get_temp_by_date(data, date):
    for forecast in data["list"]:
        if date in forecast["dt_txt"]:
            return forecast["main"]["temp"]
    return None

def get_wind_speed_by_date(data, date):
    for forecast in data["list"]:
        if date in forecast["dt_txt"]:
            return forecast["wind"]["speed"]
    return None

def get_pressure_by_date(data, date):
    for forecast in data["list"]:
        if date in forecast["dt_txt"]:
            return forecast["main"]["pressure"]
    return None

if __name__ == "__main__":
    location = "London,us"
    weather_data = get_weather_data(location)

    while True:
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        option = input("Enter your choice: ")

        if option == "1":
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            temp = get_temp_by_date(weather_data, date)
            if temp is not None:
                print(f"The temperature at {date} is {temp} Kelvin.")
            else:
                print("Data not available for the given date.")
        elif option == "2":
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            wind_speed = get_wind_speed_by_date(weather_data, date)
            if wind_speed is not None:
                print(f"The wind speed at {date} is {wind_speed} m/s.")
            else:
                print("Data not available for the given date.")
        elif option == "3":
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            pressure = get_pressure_by_date(weather_data, date)
            if pressure is not None:
                print(f"The pressure at {date} is {pressure} hPa.")
            else:
                print("Data not available for the given date.")
        elif option == "0":
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")
