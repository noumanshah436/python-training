import os
from datetime import datetime
from termcolor import colored
from helper import Helper

class MonthlyOneHorizontalBarChart:
    def __init__(self, date_str, folder_name):
        self.date_str = date_str
        self.folder_name = folder_name

    def process_file(self, filename):
      try:
        with open(filename) as file:
          file.readline()
          for row in file.readlines():
            row = row.split(",")
            day = datetime.strptime(row[0], f"%Y-%m-%d").strftime(f"%d")

            if row[1] != "" and row[3] != "":
              print(f"{day} ", end="")
              self.show_bar(int(row[1]), "red")
              self.show_bar(int(row[3]), "blue")
              print(f" {int(row[3])}C - {int(row[1])}C\n")

      except FileNotFoundError:
          print("That file was not found :(")

    def show_bar(self, temp, color_code):
      for i in range(temp):
        print(colored("+", f"{color_code}"), end="")

    def display_bar_chart(self):
      file_name = Helper.get_file_name(self.date_str, self.folder_name)

      if not os.path.isfile(file_name):
        print("DATA NOT FOUND")
      else:
        self.process_file(file_name)
