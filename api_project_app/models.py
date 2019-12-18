from django.db import models

class Books(models.Model):
    book_name = models.CharField(max_length=50,null=True,blank=True)


# added comment to test the push and pull