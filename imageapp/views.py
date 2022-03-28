from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from imageapp.models import ImageModel
from imageapp.serializers import ImageSerializer
from imageapp.services import download_image, resize_image


class ImageViewSet(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.CreateModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    serializer_class = ImageSerializer
    queryset = ImageModel.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data
        # Сохраняем картинку и возвращаем параметры для добавления в БД
        name, url, picture, width, height = download_image(data["url"])
        new_image = ImageModel(name=name,
                               url=url,
                               picture=picture,
                               width=width,
                               height=height)
        new_image.save()

        data = {
            "id": new_image.pk,
            "name": name,
            "url": url,
            "picture": picture,
            "width": width,
            "height": height
        }
        return Response(data=data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'], url_path=r'(?P<pk>\d+/resize)', name='resize image')
    def resize(self, request, pk):
        pk = int(pk.split('/')[0])  # Получаем pk
        name = ImageModel.objects.filter(id=pk).first()  # Получаем имя фото по pk

        # Получаем новый width из запроса пользователя
        if request.data["width"] is None:
            width = int(name.width)
            print(width)
            print(type(width))
        else:
            width = int(request.data["width"])
            print('else', width)

        # Получаем новый height из запроса пользователя
        if request.data["width"] is None:
            height = int(name.height)
            print(height)
            print(type(height))
        else:
            height = int(request.data["height"])
            print('else', height)

        resize_path = resize_image(width, height, name)  # Передаем в функцию преобразования
        new_name = resize_path.split('\\')[-1]  # Возвращаем путь новой картинки

        new_image = ImageModel(name=new_name,
                               url=None,
                               picture=resize_path,
                               width=width,
                               height=height,
                               parent_picture=pk)
        new_image.save()  # Сохраняем измененную картинку как новую с указанием id родительской картинки

        return Response(data={"width": width, "height": height}, status=status.HTTP_200_OK)

