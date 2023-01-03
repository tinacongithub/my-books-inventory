from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=200)
    year_published = models.IntegerField()
    
    def __str__(self):
      return f"{self.title}, {self.author}, {self.year_published}, {self.id}"
