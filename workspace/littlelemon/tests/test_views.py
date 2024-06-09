from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setup(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
    def test_getall(self):
        queryset = Menu.objects.all()
        serializer_class = MenuSerializer
