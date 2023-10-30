# Original data
original_data = "Run Mon, 10/30/2023 Afternoon Run 18:57 4.01 km"

# Split the original data into parts
parts = original_data.split()

# Extract the date components and time
day = parts[1]
date = parts[2]
time = parts[5]

print(parts)
print(date)

# Split the date into month, day, and year
month, day, year = date.split('/')

activity = parts[0]

# Convert the date components into the desired format
formatted_date = f'"{month} {day}, {year}, {time} PM"'

# Reorganize the data
new_data = f'{formatted_date},{activity},{day}'

print(new_data)
