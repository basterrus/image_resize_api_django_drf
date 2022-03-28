from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory
from imageapp.views import ImageViewSet


class ImagesApplication(TestCase):
    """Тест кейс проверки api"""

    def setUp(self) -> None:
        self.url = 'https://www.notebookcheck-ru.com/fileadmin/_migrated/pics/eee_2_02.jpg'

    def test_get_all_images(self):
        """Тест проверяет доступность указанного адреса"""

        factory = APIRequestFactory()
        request = factory.get('/api/images/')
        images_view = ImageViewSet.as_view({'get': 'list'})
        response = images_view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_images(self):
        """Тест проверяет возможность создания записей"""

        factory = APIRequestFactory()
        request = factory.post('/api/images/', {"url": self.url})
        images_view = ImageViewSet.as_view({'post': 'create'})
        response = images_view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_images_from_db(self):
        """Тест проверяет возможность удаления записи"""

        factory = APIRequestFactory()
        request = factory.delete(f'/api/images/{1}/')
        images_view = ImageViewSet.as_view({'delete': 'list'})
        response = images_view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def tearDown(self) -> None:
        pass
