import requests

r = requests.post('https://httpbin.org/post', data={'data': 'A message from CS361'})

print(r.text)