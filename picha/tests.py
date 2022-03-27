from django.test import TestCase
from .models import Image,Category,Location

class ImageTestClass(TestCase):
    
    def setUp(self):

    # Set up method
        self.new_category = Category(name='Wildlife')
        self.new_category.save_category()
            
        self.new_location = Location(city='Nairobi', country='Kenya')
        self.new_location.save_location()
            
        self.new_picture = Image(img='images/py.jpeg', name='Lion', description='jungle', category=self.new_category, location=self.new_location)
        self.new_picture.save_image()
        
       
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_picture,Image))
        self.assertTrue(isinstance(self.new_category, Category))
        self.assertTrue(isinstance(self.new_location, Location))   
          
    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()   
    def test_save_image(self):
        self.assertTrue(len(Image.objects.all()) == 1)

    def test_delete_image(self):
        self.new_picture.delete_image()
        self.assertTrue(len(Image.objects.all()) == 0)
        
    # def test_search_image(self):
    #     '''
    #     test method to ensure correct searching of an multiple image instances by category
    #     '''
    #     self.new_picture = Image.search_by_category(self.new_picture.category)

    def test_filter_by_location(self):
        self.new_picture = Image.filter_by_location(self.new_picture.location)
        print(self.new_picture)
    def test_get_image_by_id(self):
        self.new_picture = Image.get_image_by_id(self.new_picture.id)
    def test_update_image(self):
        update_test = self.new_picture.update_image('images/jolly.png')
        self.assertEqual(update_test.image_link, 'images/jolly.png')
        
class CategoryTestClass(TestCase):
    '''
    '''
    def setUp(self):
        self.new_category = Category(name='Wildlife')
        self.new_category.save_category()
    def tearDown(self):
        Category.objects.all().delete()
    def test_delete_category(self):
        self.new_category.save_category()
        self.new_category.delete_category()
        self.assertTrue(len(Category.objects.all()) == 0)

    def test_save_category(self):
        self.assertTrue(len(Category.objects.all()) == 1)   
   
    def test_update_category(self):
        update_test = self.new_category.update_category('Wildlife','Beach')
        self.assertEqual(update_test.name, 'Beach')
    
class LocationTestClass(TestCase):
    '''
    test class for Locations model
    '''
    def setUp(self):
        self.new_location = Location(city='Tokyo', country='Japan')
        self.new_location.save_location()

    def test_save_location(self):
        self.assertTrue(len(Location.objects.all()) == 1)     

    def test_delete_location(self):
        self.new_location.save_location()
        self.new_location.delete_location()
        self.assertTrue(len(Location.objects.all()) == 0)

    def test_update_location(self):
        update_location = Location.update_location('Japan', 'Shree')
        self.assertEqual(update_location.city, 'Shree')
        