import requests

# requests.get() -> HTTP GET method
# requests.post(), requests.delete()

url = 'https://example.com/'

response = requests.get(url)

print(response)
# expected <Response [200]>

print(type(response))
# expected <class 'requests.models.Response'

print(response.url)
# https://example.com/

print (response.status_code)
# 200

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

print(response.headers['Content-Type'])
print(response.headers['content-type'])

print(response.encoding)

print('\n\n\n---body---')

print(response.text)