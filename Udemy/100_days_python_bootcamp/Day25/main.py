#Day 25 of 100
#reading from a csv file

# with open("weather_data.csv") as file:
#     data = file.readlines()
#
# clean_data = []
# for raw_data in data:
#     clean_word = raw_data.split()   # this removes the new line at the end of line
#     clean_data.append(clean_word)
#
# print(clean_data)

# using the in built csv library
# import csv
#
# with open("weather_data.csv") as data_file:
#     temperatures = []
#     data = csv.reader(data_file)    # This returns a list of the items in rows
#
#     for temperature in data:
#         if temperature[1] == 'temp':
#             continue
#         else:
#             temperatures.append(int(temperature[1]))
#
# print(temperatures)

#using pandas

import pandas

data = pandas.read_csv("weather_data.csv")
squirrel_data = pandas.read_csv("Squirrel_Data.csv")

fur_color = squirrel_data["Primary Fur Color"]
gray = 0
red = 0
black = 0

for fur_c in fur_color:
    if fur_c == "Gray":
        gray += 1
    elif fur_c == "Cinnamon":
        red += 1
    elif fur_c == "Black":
        black += 1

squirrel_dict = {
                "Fur Color": ["gray", "red", "black"],
                "Count": [gray, red, black]
}

final_data = pandas.DataFrame(squirrel_dict)
final_data.to_csv("squirrel_color.csv")
#squirrel_data_frame = squirrel_dict.Dataframe()

# print(round(data["temp"].mean(), 2))    #displaying the average temperature
# print(data["temp"].max())               #displaying the maximum temperature
#
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]     #converting celcius to farenheit
# print((monday.temp*9/5) + 32)




