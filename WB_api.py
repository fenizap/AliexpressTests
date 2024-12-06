from dataclasses import asdict

import requests
import json

# Получение всех товаров
def get_items ():
    items = requests.get('https://recom.wb.ru/personal/ru/common/v5/search?ab_testing=false&appType=1&curr=rub&dest=-1257786&page=1&query=0&resultset=catalog&spp=30&suppressSpellcheck=false').json()
    for item in items['data']['products']:
        print(item['name'])

#get_items()

# Поиск по строке "Водолазка", прикрутить поиск по любой строке
def search_item ():
    search_result = requests.get('https://search.wb.ru/exactmatch/ru/male/v9/search?ab_testid=boost_promo_5&appType=1&curr=rub&dest=12358082&fbrand=29825&fkind=1&hide_dtype=10&lang=ru&page=1&query=%D0%92%D0%BE%D0%B4%D0%BE%D0%BB%D0%B0%D0%B7%D0%BA%D0%B0&resultset=catalog&sort=popular&spp=30&suppressSpellcheck=false&uclusters=2&xsubject=153').json()
    listofgoods = []
    for result in search_result ['data']['products']:
# Добавить обработку случая, если нет товаров с нужным рейтингом
        if result['nmReviewRating'] >= 4.8:
            aboba = result['id']
            listofgoods.append(aboba)
    return listofgoods

#print(search_item())

#Добавление полученных товаров в корзину

def add_to_cart (listofgoods):


