import pandas as pd

raw_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

new_data = raw_data["Primary Fur Color"].value_counts().rename_axis('Fur Color').reset_index(name='Quantity')
new_data.to_csv("squirrels_colors_count.csv")
print(new_data)

#
# # data = pd.read_csv("weather_data.csv")
# # print(data["temp"].mean())
# # max_temp = data["temp"].max()
# # # print(data["temp"].max())
# #
# # print(data[data.day == "Monday"])
# # print(data[data.temp == max_temp])
# #
# # monday = data[data.day == "Monday"]
# # print(monday.temp)
#
# data_dict = {
#     "students": ["Igor", "Nastya", "Alex"],
#     "scores": [100, 90, 80]
# }
#
# data = pd.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# print(data)
#
#
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     print(type(data))
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #
# # print(data)
# # print(temperatures)