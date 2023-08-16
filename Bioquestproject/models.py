from django.db import models
from PIL import Image
from django.db import models

class Option(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Categories(models.Model):
    category = models.CharField(max_length=50, blank=False, null=False)
    image = models.ImageField(default='default.jpg', upload_to='static/category_pics')

    def __str__(self):
        return 'Category Pic'

    # Resizing big image
    def save(self):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 250 or img.width > 250:
            output_size = (250, 250)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Products(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    variety = models.CharField(max_length=50, blank=False, null=False, default='category')
    description = models.CharField(max_length=250, blank=False, null=False)
    image = models.ImageField(default='default.jpg', upload_to='static/products_pics')
    photoname = models.CharField(max_length=50)


    def __str__(self):
        return 'Product Pic'

    # Resizing big image


class Customers(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    phone  = models.IntegerField( blank=False, null=False)
    email = models.CharField( max_length=50,blank=False, null=False)




def __str__(self):
    return self.name




