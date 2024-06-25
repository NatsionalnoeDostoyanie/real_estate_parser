import json

import scrapy
from requests import Request
from inline_requests import inline_requests
from scrapy_selenium import SeleniumRequest


class RealEstateSpider(scrapy.Spider):
    name = "real_estate_spider"

    def __init__(
            #  Many more params could be added here
            self,
            offset=0,
            limit=999999999,
            sort_field='obj_publ_dt',
            sort_type='desc',
            place='0-1',
            collect_extra_data='true',
            *args,
            **kwargs,
    ):
        super(RealEstateSpider, self).__init__(*args, **kwargs)
        self.offset = offset
        self.limit = limit
        self.sort_field = sort_field
        self.sort_type = sort_type
        self.place = place

        if collect_extra_data.lower() == 'true':
            self.collect_extra_data = True
        elif collect_extra_data.lower() == 'false':
            self.collect_extra_data = False

        self.BASE_URL = 'https://наш.дом.рф/сервисы/api/kn/object/'

        if self.collect_extra_data:
            self.EXTRA_DATA_BASE_URL = 'https://наш.дом.рф/сервисы/api/object/'

    def start_requests(self):
        #  Many more params could be added here
        params = {
            'offset': self.offset,
            'limit': self.limit,
            'sortField': self.sort_field,
            'sortType': self.sort_type,
            'place': self.place,
        }
        primary_data_url = Request('GET', self.BASE_URL, params=params).prepare().url
        yield SeleniumRequest(
            url=primary_data_url,
            callback=self.parse,
        )

    @inline_requests
    def parse(self, response):
        primary_data_json = json.loads(response.xpath('//body//text()').get())
        primary_items_list = primary_data_json['data']['list']

        if self.collect_extra_data:
            raw_items_list = []
            for item in primary_items_list:
                try:
                    extra_item_url = f'{self.EXTRA_DATA_BASE_URL}{str(item["objId"])}'
                    resp = yield SeleniumRequest(url=extra_item_url)
                    data_json = json.loads(resp.xpath('//body//text()').get())
                    raw_extra_item = data_json['data']
                    raw_items_list.append(raw_extra_item)
                except Exception as e:
                    print(f'Error processing URL {extra_item_url}: {e}')
                    continue
            fields = [
                'nameObj',
                'address',
                'id',
                'objReady100PercDt',
                'developer.devFullCleanNm',
                'developer.developerGroupName',
                'objPublDt',
                'objTransferPlanDt',
                'objPriceAvg',
                'soldOutPerc',
                'objLkClassDesc',
                'objElemLivingCnt',
            ]
        else:
            raw_items_list = primary_items_list
            fields = [
                'objCommercNm',
                'objAddr',
                'objId',
                'objReady100PercDt',
                'developer.fullName',
            ]

        field_translations = {
            'objCommercNm': 'Заголовок объявления',
            'objAddr': 'Адрес',
            'objId': 'ID объявления',
            'objReady100PercDt': 'Ввод в эксплуатацию',
            'developer.fullName': 'Застройщик',

            'nameObj': 'Заголовок объявления',
            'address': 'Адрес',
            'id': 'ID объявления',
            'developer.devFullCleanNm': 'Застройщик',
            'developer.developerGroupName': 'Группа компаний',
            'objPublDt': 'Дата публикации проекта',
            'objTransferPlanDt': 'Выдача ключей',
            'objPriceAvg': 'Средняя цена за 1 м²',
            'soldOutPerc': 'Распроданность квартир',
            'objLkClassDesc': 'Класс недвижимости',
            'objElemLivingCnt': 'Количество квартир',
        }
        processed_items_list = []
        for item in raw_items_list:
            processed_item = {}
            for field in fields:
                keys = field.split('.')  # 'developer.fullName' -> ['developer', 'fullName']
                value = item
                for key in keys:
                    value = value.get(key, '')

                if field in field_translations:
                    processed_item[field_translations[field]] = value
            processed_items_list.append(processed_item)

        with open("processed_items_list.json", "w", encoding="utf-8") as file:
            json.dump(processed_items_list, file)
