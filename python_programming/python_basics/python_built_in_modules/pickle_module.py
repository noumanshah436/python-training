# Pickling: Serializing an object (list, dict, etc.) into a string representation that can be saved to a file.
# Unpickling: Reversing the process, converting the string representation back into the object.

# *******************************************************

# Python pickle module is used for serializing and de-serializing a Python object structure.
# Any object in Python can be pickled so that it can be saved on disk.
# What pickle does is that it “serializes” the object first before writing it to file.
# Pickling is a way to convert a python object (list, dict, etc.) into a character stream.
# The idea is that this character stream contains all the information necessary to reconstruct
#      the object in another python script.


import pickle


# Pickling a python object

cars = ["Audi", "BMW", "Maruti Suzuki", "Harryti Tuzuki"]
file = "mycar.pkl"
fileobj = open(file, 'wb')
pickle.dump(cars, fileobj)
fileobj.close()


# file = "mycar.pkl"
# fileobj = open(file, 'rb')
# mycar = pickle.load(fileobj)
# print(mycar)
# print(type(mycar))


# pickle.loads = ?


# *******************************************************

# Python3 program to illustrate store
# efficiently using pickle module
# Module translates an in-memory Python object
# into a serialized byte stream—a string of
# bytes that can be written to any file-like object.


# def storeData():
#     # initializing data to be stored in db
#     Omkar = {'key': 'Omkar', 'name': 'Omkar Pathak',
#              'age': 21, 'pay': 40000}
#     Jagdish = {'key': 'Jagdish', 'name': 'Jagdish Pathak',
#                'age': 50, 'pay': 50000}
#
#     # database
#     db = {}
#     db['Omkar'] = Omkar
#     db['Jagdish'] = Jagdish
#
#     # Its important to use binary mode
#     dbfile = open('examplePickle', 'ab')
#
#     # source, destination
#     pickle.dump(db, dbfile)
#     dbfile.close()
#
#
# def loadData():
#     # for reading also binary mode is important
#     dbfile = open('examplePickle', 'rb')
#     db = pickle.load(dbfile)
#     for keys in db:
#         print(keys, '=>', db[keys])
#     dbfile.close()
#
#
# if __name__ == '__main__':
#     storeData()
#     loadData()


# **************************************************
# Pickling without a file

# # initializing data to be stored in db
# Omkar = {'key' : 'Omkar', 'name' : 'Omkar Pathak',
# 'age' : 21, 'pay' : 40000}
# Jagdish = {'key' : 'Jagdish', 'name' : 'Jagdish Pathak',
# 'age' : 50, 'pay' : 50000}
#
# # database
# db = {}
# db['Omkar'] = Omkar
# db['Jagdish'] = Jagdish
#
# # For storing
# b = pickle.dumps(db)	 # type(b) gives <class 'bytes'>
#
# # For loading
# myEntry = pickle.loads(b)
# print(myEntry)
