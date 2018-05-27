from django.db import models

# class is for table
class Post(models.Model):
    title = models.CharField(max_length=140) # this are the columns
    body = models.TextField() # columns vars are associatted with datatype field
    date = models.DateTimeField()
    
    def __str__(self):
        return self.title
    