import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter - ')
info = json.loads(urllib.request.urlopen(url).read())

comm=info['comments']
counts_list = [int(items['count']) for items in comm]
print(sum(counts_list))