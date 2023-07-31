import os

class Helper:
    @staticmethod
    def get_month(num):
      months = {
        1: 'Jan',
        2: 'Feb',
        3: 'Mar',
        4: 'Apr',
        5: 'May',
        6: 'Jun',
        7: 'Jul',
        8: 'Aug',
        9: 'Sep',
        10: 'Oct',
        11: 'Nov',
        12: 'Dec',
      }

      return months.get(num, 'Invalid Month')

    @staticmethod
    def get_file_name(date_str, folder_name):
      year, month = date_str.split('/')
      month = Helper.get_month(int(month))

      dir_list = os.listdir(folder_name)
      files = [file_name for file_name in dir_list if (year in file_name and month in file_name)]

      if len(files) > 0:
        return os.path.join(folder_name, files[0])
      else:
        return ''

    @staticmethod
    def get_files(year, folder_name):
      if not os.path.exists(folder_name):
        return []

      dir_list = os.listdir(folder_name)
      files = [file_name for file_name in dir_list if year in file_name]

      return files
