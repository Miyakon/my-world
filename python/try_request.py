import requests

# requests.get() -> HTTP GET method
# requests.post(), requests.delete()

url = 'https://example.com/'

response = requests.get(url)

print(response)
# <Response [200]>

print(type(response))
# <class 'requests.models.Response'>