from django.db import models


class Item(models.Model):
    image_src = models.ImageField(upload_to='images')
    title = models.CharField(max_length=200)
    label = models.ManyToManyField('Label')

    def __str__(self):
        return self.title
    


class Label(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
