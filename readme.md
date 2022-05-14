# Тестовое задание на позицию Python Developer
## API сервис позволяет загружать изображения по ссылке и сохраняет данные о нем в базу данных. Изменяет размеры изображения при помощи библиотеки Pillow
___

### Входные данные: 
    `{"url": "https://ichef.bbci.co.uk/news/640/cpsprodpb/14236/production/_104368428_gettyimages-543560762.jpg"}`          
### Выходные данные:
               `{"id": 2, 
               "name": "_104368428_gettyimages-543560762.jpg",
               "url": "https://ichef.bbci.co.uk/news/640/cpsprodpb/14236/production/_104368428_gettyimages-543560762.jpg",
               "picture": "http://localhost:8000/m/site_media/_104368428_gettyimages-543560762.jpg",
               "width": 640,
               "height": 360,
               "parent_picture": null }`
___
### Запуск проекта:
1. Клонировать репозиторий `https://contest.idacloud.ru/basterrus/image_resize_api_django_drf.git`
2. Перейти в каталог `cd image_resize_api_django_drf` при необходимости
3. Создать и активировать виртуальное окружение
4. Выполнить команду `pip freeze > requirements.txt`
5. Выполнить команду `python manage.py runserver`
6. Выполнить запросы к backend при помощи postman или открыть в браузере `http://127.0.0.1:8000/api/images/`
___
### Запросы к backend:
1. `GET` Список всех изображений содержащихся в базе данных по адресу `http://127.0.0.1:8000/api/images/`
2. `GET` Детальная информация об изображении по адресу `http://127.0.0.1:8000/api/images/<id>/` где id целое число, id изображения в БД
3. `POST` Изменение разрешения фото `http://127.0.0.1:8000/api/images/<id>/resize/` в теле передаем параметры width и height. 
Не записал условие при котором одно из значений будет равно None
4. `DELETE` Удаление `http://127.0.0.1:8000/api/images/<id>/` где id целое число, id изображения в БД которое нужно удалить.
Не предусмотрел удаление поля родительской зависимости из БД если она есть
