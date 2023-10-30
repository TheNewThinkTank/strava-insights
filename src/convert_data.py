
original_data = "Run Mon, 10/30/2023 Afternoon Run 18:57 4.01 km"

parts = original_data.split()

day = parts[1]
date = parts[2]
time = parts[5]

print(parts)
# print(date)

month, day, year = date.split('/')

activity = parts[0]

formatted_date = f'"{month} {day}, {year}, 00:00:00 PM"'

new_data = f'{formatted_date},{activity},{day}'

print(new_data)
