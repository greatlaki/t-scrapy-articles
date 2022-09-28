import requests
from openpyxl import load_workbook
from requests import Response
from rest_framework import status
from rest_framework.views import APIView


class ListArticles(APIView):

    def post(self, request):
        json_response = []

        file = request.data.get('file')
        if not file:
            return Response({"Error": "You must upload a file"})

        articles = xlsx_to_tuple(file=file)

        if len(json_response) == 1:
            json_response = json_response[0]

        return Response(json_response)


def get_product_data(article):

    response = requests.get(
        f'https://basket-01.wb.ru/vol{str(article)[:3]}/part{str(article)[:5]}/{article}/info/ru/card.json'
    )
    if response.status == status.HTTP_200_OK:
        result = response.json()
        article = result.get('nm_id')
        brand = result.get('selling').get('brand_name')
        title = result.get('imt_name')
    return {'Article': article, 'Brand': brand, 'Title': title}


def xlsx_to_tuple(file):
    wb = load_workbook(file)
    sheet = wb.get_sheet_by_name('Sheet1')
    articles = tuple(map(lambda x: int(x[0]), sheet.values))

    return articles
