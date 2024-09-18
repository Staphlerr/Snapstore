from django.test import TestCase, Client
from django.utils import timezone
from .models import ItemEntry

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'product.html')

    def test_nonexistent_page(self):
        response = Client().get('/skibidi/')
        self.assertEqual(response.status_code, 404)

    def test_strong_mood_user(self):
        now = timezone.now()
        item = ItemEntry.objects.create(
          name="Tas Ace Hardware",
          date = now,
          description = "bisa buat bawa londrian 6,5 kg",
          price = 7000,
        )
        self.assertTrue(item.is_price_expensive)