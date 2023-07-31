import os
from datetime import datetime
from helper import Helper

class MonthlyWeatherReport:
    def __init__(self, date_str, folder_name):
        self.date_str = date_str
        self.folder_name = folder_name

        self.high_tem = {"sum": 0, "row_count":0}
        self.low_tem = {"sum": 0, "row_count":0}
        self.most_humid = {"sum": 0, "row_count":0}

    def process_file(self, filename):
      try:
        with open(filename) as file:
          file.readline()

          for row in file.readlines():
            row = row.split(",")

            if row[1] != "":
              self.high_tem["sum"] += int(row[1])
              self.high_tem["row_count"] += 1

            if row[3] != "":
              self.low_tem["sum"] += int(row[3])
              self.low_tem["row_count"] += 1

            if row[7] != "":
              self.most_humid["sum"] += int(row[7])
              self.most_humid["row_count"] += 1

      except FileNotFoundError:
          print("That file was not found :(")


    def get_monthly_info(self):
      file_name = Helper.get_file_name(self.date_str, self.folder_name)

      if not os.path.isfile(file_name):
        print("DATA NOT FOUND")
      else:
        self.process_file(file_name)
        self.display_report()

    def display_report(self):
      print(f"Highest Average: {self.high_tem['sum'] // self.high_tem['row_count']}C")
      print(f"Lowest Average: {self.low_tem['sum'] // self.low_tem['row_count']}C")
      print(f"Average Humidity: {self.most_humid['sum'] // self.most_humid['row_count']}%")
