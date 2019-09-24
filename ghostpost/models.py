from django.db import models 
from django.contrib.auth.models import User


class AnonUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user


class Boast(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    boast = models.CharField(max_length=280)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    updated_timestamp = models.DateTimeField(auto_now = True)
    # upvotes = models.ManyToManyField(AnonUser, related_name="boast_upvotes")
    # downvotes = models.ManyToManyField(AnonUser, related_name="boast_downvotes")
    
    def __str__(self):
        return f"{self.boast} {self.timestamp}"
  
    
class Roast(models.Model):
    user=models.ForeignKey(AnonUser, on_delete=models.CASCADE)
    roast = models.CharField(max_length=280)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    updated_timestamp = models.DateTimeField(auto_now = True)
    # upvotes = models.ManyToManyField(AnonUser, related_name="roast_upvotes")
    # downvotes = models.ManyToManyField(AnonUser, related_name="roast_downvotes")
    
    def __str__(self):
        return f"{self.roast} {self.timestamp}"
    
class Vote(models.Model):
    roast_upvote = models.ManyToManyField(Roast, related_name="roast_upvotes")
    roast_downvote = models.ManyToManyField(Roast, related_name="roast_downvotes")
    boast_upvote = models.ManyToManyField(Boast, related_name="roast_upvotes")
    boast_downvote = models.ManyToManyField(Boast, related_name="roast_downvotes")
    