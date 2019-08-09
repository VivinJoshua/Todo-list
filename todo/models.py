from django.db import models

# Create your models here.
class todoItem(models.Model):
    content=models.TextField(max_length=200)
    def __str__(self):
        return self.content
