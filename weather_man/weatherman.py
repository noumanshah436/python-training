import sys, os
from yearly_weather_report import *
from monthly_weather_report import *
from monthly_horizontal_bar_chart import *
from monthly_one_horizontal_bar_chart import *


def weatherman():
  if len(sys.argv) != 4:
    print("Please give valid environment variables")
    return

  flag = sys.argv[1]
  date = sys.argv[2]
  folder_name = sys.argv[3]

  if not os.path.exists(folder_name):
    print("That location doesn't exist!")
    return

  if flag == '-e':
    yearly_info = YearlyWeatherReport(date, folder_name)
    yearly_info.get_yearly_info()
  elif flag == '-a':
    monthly_info = MonthlyWeatherReport(date, folder_name)
    monthly_info.get_monthly_info()
  elif flag == '-c':
    monthly_info = MonthlyHorizontalBarChart(date, folder_name)
    monthly_info.display_bar_chart()
  elif flag == '-b':
    monthly_info = MonthlyOneHorizontalBarChart(date, folder_name)
    monthly_info.display_bar_chart()

weatherman()
