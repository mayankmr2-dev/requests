import requests
k = {"key1": "value1"}
r = requests.get("https://httpbin.org/get", params=k)
print(r.status_code)  # 200 - successful
# print(r.text)
print(type(r.text))  # <class 'str'>
rk = r.json()
print(rk)
print(type(rk))   # <class 'dict'>
print("########################")
# print(rk['headers'])
for k, v in rk.items():
    print("{} : {}".format(k, v))

"""
Output - 
args : {}
headers : {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.22.0', 'X-Amzn-Trace-Id': 'Root=1-5f97edf8-0c1744f43ccdbbda4eac510f'}
origin : 103.195.202.25
url : https://httpbin.org/get
"""
