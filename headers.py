import requests
k = {"key1": "value1"}
r = requests.get("https://httpbin.org/get", params=k)
head = r.headers
for k, v in head.items():
    print("{} : {}".format(k, v))

'''
OUTPUT - 
Date : Tue, 27 Oct 2020 11:01:14 GMT
Content-Type : application/json
Content-Length : 344
Connection : keep-alive
Server : gunicorn/19.9.0
Access-Control-Allow-Origin : *
Access-Control-Allow-Credentials : true
'''
'''
s = requests.session()
r = requests.get('https://httpbin.org/cookies/set/Mayan_legend/12345')
print(r.text)
'''
# {
#     "cookies": {
#         "Mayan_legend": "12345"
#     }
# }
'''
print(r.json()['cookies'])  # {'Mayan_legend': '12345'}


'''
