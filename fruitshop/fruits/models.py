from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.PositiveBigIntegerField()
    img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
    