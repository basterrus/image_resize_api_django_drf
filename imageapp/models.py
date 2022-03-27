from django.db import models


class ImageModel(models.Model):
    name = models.CharField(max_length=256, verbose_name='Имя')
    url = models.URLField(blank=True, null=True)
    picture = models.CharField(max_length=256, blank=True, verbose_name='Изображение')
    width = models.IntegerField(verbose_name='Ширина', blank=True, null=True)
    height = models.IntegerField(verbose_name='Длина', blank=True, null=True)
    parent_picture = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}'
