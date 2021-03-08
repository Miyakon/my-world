import requests

url = 'https://api.gnavi.co.jp/RestSearchAPI/v3/'
params = {}
params['keyid'] = 'accesskey'
params['freeword'] = '神田駅，肉'

response = requests.get(url, params)

print(response)
