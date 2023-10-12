# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()
# print(data)

# import csv
#
# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         temperatures.append(row[1])
#     for i in range(1, len(temperatures)):
#         temperatures[i] = int(temperatures[i])
#     print(temperatures)
#

# import pandas
#
# data = pandas.read_csv("weather_data.csv")
#
# data_dict = data.to_dict()
# print(data_dict)

# # data_list = data["temp"].to_list()
# # print(data_list)
# #
# # print(data["temp"].mean())
# #
# # print(data["temp"].max())
#
# # print(data.temp)
#
# # print(data[data.day == 'Monday'])
# # print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == 'Monday']
# monday_temp = monday.temp
# converted = (monday_temp * 1.8) + 32
# print(converted)

import pandas

























# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
# print(gray_squirrels_count)
# print(red_squirrels_count)
# print(black_squirrels_count)
#
# census_count_color = {
#     'Fur Color': ['Gray', 'Cinnamon', 'Black'],
#     'Counts': [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
# }
#
# counts = pandas.DataFrame(census_count_color)
# print(counts)
#
# counts.to_csv('Squirrel_count.csv')
