from collections.abc import Iterable
from django.db import models
from django.utils.text import slugify
# Create your models here.
class Location(models.Model):
    street =  models.CharField(max_length =200)
    city  = models.CharField(max_length =200)
    state = models.CharField(max_length =200)
    country = models.CharField(max_length =200)
    zip = models.CharField(max_length =200)

class Author(models.Model):
    name = models.CharField(max_length =200)
    company = models.CharField(max_length =200)
    designation = models.CharField(max_length =200)

class jobPost(models.Model):
    title = models.CharField(max_length= 200)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    expire = models.DateField(null = True)
    salary = models.IntegerField()
    slug = models.SlugField(null=True,max_length= 40,unique = True)
    location = models.OneToOneField(Location,null = True ,on_delete = models.CASCADE)
    author = models.ForeignKey(Author,on_delete = models.CASCADE)

    def save(self, *args, **kwargs):
        # if not self.id:
        self.slug = slugify(self.title)
        return super(jobPost,self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.title} Company in SX'
    

