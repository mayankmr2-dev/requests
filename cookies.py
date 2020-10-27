import requests
cookies = {"k": "v"}
r = requests.get("https://httpbin.org/cookies", cookies=cookies)
print(type(r.text))  # <class 'str'>
print(r.json())  # {'cookies': {'k': 'v'}}

# in the get method
"""
cookies = {"k": "v"}
r = requests.get("https://httpbin.org/get", cookies=cookies)
print(type(r.text))  # <class 'str'>
print(r.json())  # {'cookies': {'k': 'v'}}
print(r.cookies)

"""
