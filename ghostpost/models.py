from django.db import models 
from django.contrib.auth.models import User

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    bio = models.TextField(max_length=300)

    def __str__(self):
        return self.name
    
class Boast(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # post = models.TextField(max_length=280)
    boast = models.ManyToManyField(Author, max_length = 280, related_name="boasts")
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    updated_timestamp = models.DateTimeField(auto_now = True)
    def __str__(self):
        return f"{self.boast} {self.timestamp}"
  
    
class Roast(models.Model):
    author=models.ForeignKey(Author, on_delete=models.CASCADE)
    # post = models.TextField(max_length=280)
    roast = models.ManyToManyField(Author, max_length=280, related_name="roasts")
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    updated_timestamp = models.DateTimeField(auto_now = True)
    def __str__(self):
        return f"{self.roast} {self.timestamp}"