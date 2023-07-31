import os
from datetime import datetime
from helper import Helper

class YearlyWeatherReport:
    def __init__(self, year, folder_name):
        self.year = year
        self.folder_name = folder_name

        self.high_tem = {}
        self.low_tem = {}
        self.most_humid = {}

    def __process_file(self, filename):
      try:
        with open(filename) as file:
          file.readline()

          high_temp, low_temp, most_humid = self.__get_initial_data()

          for row in file.readlines():
            row = row.split(",")

            self.__process_high_temperature(row, high_temp)
            self.__process_low_temperature(row, low_temp)
            self.__process_most_humid(row, most_humid)

          self.__update_temp(high_temp, low_temp, most_humid)

      except FileNotFoundError:
        print("That file was not found :(")

    def __get_initial_data(self):
      return {"temp": 0, "day": ""}, {"temp": 100, "day": ""}, {"humidity": 0, "day": ""}

    def __process_high_temperature(self, row, high_temp):
      if row[1] and int(row[1]) > high_temp["temp"]:
        high_temp["temp"] = int(row[1])
        high_temp["day"] = datetime.strptime(row[0], "%Y-%m-%d").strftime("%B %d")

    def __process_low_temperature(self, row, low_temp):
      if row[3] and int(row[3]) < low_temp["temp"]:
        low_temp["temp"] = int(row[3])
        low_temp["day"] = datetime.strptime(row[0], "%Y-%m-%d").strftime("%B %d")

    def __process_most_humid(self, row, most_humid):
      if row[7] and int(row[7]) > most_humid["humidity"]:
        most_humid["humidity"] = int(row[7])
        most_humid["day"] = datetime.strptime(row[0], "%Y-%m-%d").strftime("%B %d")

    def __update_temp(self, high_temp, low_temp, most_humid):
      self.high_tem.update({high_temp['temp']: high_temp['day']})
      self.low_tem.update({low_temp['temp']: low_temp['day']})
      self.most_humid.update({most_humid['humidity']: most_humid['day']})

    def get_yearly_info(self):
      files = Helper.get_files(self.year, self.folder_name)

      if len(files) == 0:
        print("DATA NOT FOUND")
        return

      for file in files:
        if not os.path.isfile(f"{self.folder_name}/{file}"):
          next
        else:
          self.__process_file(f"{self.folder_name}/{file}")

      self.display_report()

    def display_report(self):
      max_tem = max(self.high_tem.keys())
      min_tem = min(self.low_tem.keys())
      most_humid = max(self.most_humid.keys())

      print(f"Highest: {max_tem}C on {self.high_tem[max_tem]}")
      print(f"Lowest: {min_tem}C on {self.low_tem[min_tem]}")
      print(f"Humid: {most_humid}% on {self.most_humid[most_humid]}")
