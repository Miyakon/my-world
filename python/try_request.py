import requests
import urllib

# requests.get() -> HTTP GET method
# requests.post(), requests.delete()

url = 'https://example.com/'

response = requests.get(url)
print('\n\n -- request headers -- ')
print(response.request.headers)
print('\n\n')
print(response.request)

print(response)
# expected <Response [200]>

print(type(response))
# expected <class 'requests.models.Response'

print(response.url)
# https://example.com/

print (response.status_code)
# 200

print('\n\n\n---header---')
print(response.headers)
# {'Content-Encoding': 'gzip',
# 'Accept-Ranges': 'bytes',
# 'Cache-Control': 'max-age=604800',
# 'Content-Type': 'text/html',
# 'Date': 'Thu, 12 Jul 2018 11:58:54 GMT', 
# 'Etag': '"1541025663"',
# 'Expires': 'Thu, 19 Jul 2018 11:58:54 GMT',
# 'Last-Modified': 'Fri, 09 Aug 2013 23:54:35 GMT',
# 'Server': 'ECS (oxr/8313)',
# 'Vary': 'Accept-Encoding',
# 'X-Cache': 'HIT',
# 'Content-Length': '606'}

print(response.encoding)

print('\n\n\n---body---')
print(response.text)

url = 'https://www.google.co.jp/search'

params = {'q': '日本代表', 'tbm': 'nws'}

r = requests.get(url, params=params)

print(r.url)
# https://www.google.co.jp/search?q=%E6%97%A5%E6%9C%AC%E4%BB%A3%E8%A1%A8&tbm=nws

print('\n\n\n---header---')
print(r.headers)

print('\n\n\n---body---')
print(r.text)

print('\n\n\n---history---')
print(r.history)
