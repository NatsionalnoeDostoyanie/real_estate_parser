## Usage
```
scrapy crawl real_estate_spider -a limit=3
```
### response (decoded):
```json
[
  {
    "Заголовок объявления": "HideOUT",
    "Адрес": "г. Москва, район Р-н Раменки, пр-д 3-й Сетуньский",
    "ID объявления": 60425,
    "Ввод в эксплуатацию": "2028-06-30",
    "Застройщик": "СПЕЦИАЛИЗИРОВАННЫЙ ЗАСТРОЙЩИК ХАЙДАУТ",
    "Группа компаний": "Dominanta",
    "Дата публикации проекта": "2024-06-18",
    "Выдача ключей": "31-12-2028 12:00",
    "Средняя цена за 1 м²": "",
    "Распроданность квартир": "",
    "Класс недвижимости": "Элитный",
    "Количество квартир": 665
  },
  {
    "Заголовок объявления": "",
    "Адрес": "г. Москва, район Тверской р-н, пер Богоявленский, вл. 3с1",
    "ID объявления": 60273,
    "Ввод в эксплуатацию": "2028-06-30",
    "Застройщик": "СПЕЦИАЛИЗИРОВАННЫЙ ЗАСТРОЙЩИК Б-ХОЛДИНГ",
    "Группа компаний": "",
    "Дата публикации проекта": "2024-06-14",
    "Выдача ключей": "30-06-2028 12:00",
    "Средняя цена за 1 м²": "",
    "Распроданность квартир": "",
    "Класс недвижимости": "Элитный",
    "Количество квартир": 73
  },
  {
    "Заголовок объявления": "РОДИНА ПАРК",
    "Адрес": "г. Москва, ул Верейская, вл. 12",
    "ID объявления": 60247,
    "Ввод в эксплуатацию": "2026-12-31",
    "Застройщик": "СПЕЦИАЛИЗИРОВАННЫЙ ЗАСТРОЙЩИК РОДИНА ПАРК",
    "Группа компаний": "",
    "Дата публикации проекта": "2024-06-13",
    "Выдача ключей": "30-09-2027 12:00",
    "Средняя цена за 1 м²": "",
    "Распроданность квартир": "",
    "Класс недвижимости": "Бизнес",
    "Количество квартир": 308
  }
]
```