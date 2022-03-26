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