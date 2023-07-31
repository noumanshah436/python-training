import pickle
import requests

# Problem Statement:
# Use requests module to download the iris dataset
# Perform is “Pickling Iris.” For this, Check the UC Irvine Machine Learning Repository site
# to get the dataset. You can search the Iris dataset through their searchable interface. Follow the following steps
# to download the dataset:
#
# Go to https://archive.ics.uci.edu/ml/index.php
# On Most Popular Data Sets, you will see the name “Iris.”
# Open the Iris dataset.
# Click on the Data folder. A new tab will open, which contains some files.
# Click on the Iris. data file to download the text file.
# After saving Iris. data file, parse it using the split() function or using a new line approach.
#      The method of parsing is up to you.
#
# The main task is to get the list of lists that you will pickle. And after creating the pickle,
# write a code to read it. For downloading the Iris dataset, use the request module.


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
respons = requests.get(url)
respons_text = respons.text
data = respons_text.splitlines()
red = [[i] for i in data]
# pickling the python object
fileobj = open('irisData.pkl', 'wb')
pickle.dump(red, fileobj)
fileobj.close()

# Reading Of Pickel file
fileobj = open('irisData.pkl', 'rb')
data = pickle.load(fileobj)
print(data)
