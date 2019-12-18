from django.db import models

class Books(models.Model):
    book_name = models.CharField(max_length=50,null=True,blank=True)
    book_title = models.CharField(max_length=50,null=True,blank=True)
