import urllib.request
import re

pre_pattern = 'https://i.cdn.turner.com/money/.element/img/3.0/data/arrowDown.gif'

req = urllib.request.Request('https://money.cnn.com/data/premarket/')
pre_response = urllib.request.urlopen(req)
premarket_page = str(pre_response.read())

red_count = re.findall(pre_pattern, premarket_page)

if len(red_count) >= 2:
    future_result = "red"
else:
    future_result = "green"

print("Future results are " + future_result)
