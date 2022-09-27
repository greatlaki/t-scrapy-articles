import requests
from rest_framework import status


def get_product_data(article):

    response = requests.get(f'https://basket-01.wb.ru/vol{str(article)[:3]}/part{str(article)[:5]}/{article}/info/ru/card.json')
    if response.status == status.HTTP_200_OK:
        result = response.json()
        article = result.get('nm_id')
        brand = result.get('selling').get('brand_name')
        title = result.get('imt_name')
    return {'Article': article, 'Brand': brand, 'Title': title}
