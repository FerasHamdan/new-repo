from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    name=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=15)
    content=RichTextField()
    active =models.BooleanField(default=True)

    def __str__(self):
        return self.title