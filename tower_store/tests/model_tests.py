from django.test import TestCase

from tower_store.models import storeCategory, storeProduct

class TestStoreCategories(TestCase):

    def setUp(self):
        self.data1 = storeCategory.objects.create(name='django', slug='django')
    
    def test_category_model_entry(self):
        """
        Test cateogry data insertion for types and field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, storeCategory))

    def test_category_model_entry(self):
        """
        Test cateogry model default name
        """
        data = self.data1
        self.assertEqual(str(data), 'django')

class TestProductsModel(TestCase):
    def setUp(self):
        storeCategory.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
            self.data1 = storeProduct.objects.create(category_id=1, productTitle="django beginners", created_by_id=1, slug='django-beginners', productPrice='20.00', images='django')