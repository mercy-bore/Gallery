from django.db import models

class Image(models.Model):
    image_link = models.ImageField(upload_to='images/')
    name = models.CharField(max_length =30)
    description = models.TextField(max_length =30)
    category = models.ForeignKey( 'Category', on_delete=models.CASCADE,)
    location = models.ForeignKey( 'Location', on_delete=models.CASCADE,)




