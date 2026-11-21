
# Railway timetable using nested dictionaries

trains = {
    "101": {
        "name": "Chennai Express",
        "stations": [
            ("Chennai", "06:00", "06:15"),
            ("Katpadi", "08:00", "08:05"),
            ("Bangalore", "11:00", "11:15")
        ],
        "days": {"Monday", "Wednesday", "Friday"}
    },

    "102": {
        "name": "Pandian Express",
        "stations": [
            ("Chennai", "07:00", "07:10"),
            ("Villupuram", "09:00", "09:05"),
            ("Madurai", "13:00", "13:15")
        ],
        "days": {"Tuesday", "Thursday", "Saturday"}
    },

    "103": {
        "name": "Coimbatore Express",
        "stations": [
            ("Chennai", "08:00", "08:10"),
            ("Salem", "11:00", "11:05"),
            ("Coimbatore", "13:00", "13:15")
        ],
        "days": {"Monday", "Tuesday", "Friday"}
    },

    "104": {
        "name": "Kovai Express",
        "stations": [
            ("Chennai", "09:00", "09:10"),
            ("Katpadi", "11:00", "11:05"),
            ("Bangalore", "14:00", "14:15")
        ],
        "days": {"Wednesday", "Thursday", "Sunday"}
    },

    "105": {
        "name": "Nilgiri Express",
        "stations": [
            ("Chennai", "10:00", "10:10"),
            ("Salem", "13:00", "13:05"),
            ("Coimbatore", "15:00", "15:15")
        ],
        "days": {"Monday", "Friday", "Sunday"}
    }
}

# Search details
search_station = input("Enter station name: ")
search_day = input("Enter day: ")

# Find matching trains
result = []

for number, details in trains.items():
    if search_day in details["days"]:
        for station, arrival, departure in details["stations"]:
            if station.lower() == search_station.lower():
                result.append(
                    (number, details["name"], arrival, departure)
                )

# Sort trains by departure time
result = sorted(result, key=lambda x: x[3])

# Display timetable
if result:
    print("\nTrains available:")
    for number, name, arrival, departure in result:
        print("Train Number:", number)
        print("Train Name:", name)
        print("Arrival:", arrival)
        print("Departure:", departure)
        print("----------------------")
else:
    print("No trains available")
