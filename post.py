import requests
data = {"k": "v"}
r = requests.post("https://httpbin.org/post", data=data)
print(r.status_code)   # 200
print(type(r.text))     # <class 'str'>
print("######$$$$$$$$$$$######################")
rk = r.json()
for k, v in rk.items():
    print("{} : {} ".format(k, v))
print(r.url)
# print(r.json())

'''
OUTPUT -
args : {} 
data :  
files : {} 
form : {'k': 'v'} 
headers : {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Content-Length': '3', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.22.0', 'X-Amzn-Trace-Id': 'Root=1-5f97fb62-24429858063c5634475d419a'} 
json : None 
origin : 103.195.202.25 
url : https://httpbin.org/post 
https://httpbin.org/post
'''
