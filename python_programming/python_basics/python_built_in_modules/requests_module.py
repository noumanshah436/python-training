import requests

# r is the response object
# when our request success , r will get info received from server
# params convert our dictionary to query string which can be send to specified url

# payload={"first_name":"Nouman" ," last_name":"shah"}
# r=requests.get("https://httpbin.org/get" , params=payload)  
# print(r.url)  #  https://httpbin.org/get?first_name=Nouman&+last_name=shah
# print(r.status_code)
# print(r.content)  #  return response body as bytes
# print(r.text)  #  return response body as bytes


payload={"first_name":"Nouman" ," last_name":"shah"}
r=requests.post("https://httpbin.org/post" , data=payload)  
# print(r.url)  #  https://httpbin.org/get?first_name=Nouman&+last_name=shah
# print(r.status_code)
# print(r.content)  #  return response body as bytes
print(r.text)  #  return response body as bytes


# r = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
# # r = requests.get("https://financialmodelingprep.com/how-to/how-to-create-a-financial-modeling-prep-account")
# print(r.text)
# print(r.status_code)

# url = "www.something.com"
# data = {
#     "p1":4,
#     "p2":8
# }
# r2 = requests.post(url=url, data=data)
