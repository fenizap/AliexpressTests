import requests
import json

def get_items ():
    items = requests.get('https://recom.wb.ru/personal/ru/common/v5/search?ab_testing=false&appType=1&curr=rub&dest=-1257786&page=1&query=0&resultset=catalog&spp=30&suppressSpellcheck=false').json()
    for item in items['data']['products']:
        print(item['name'])

get_items()

