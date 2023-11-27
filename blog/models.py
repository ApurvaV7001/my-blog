from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS=(
    (0,"Draft"),
    (1,"Publish")
)
class Post(models.Model):
    title=models.CharField(max_length=50, unique=True)
    slug=models.CharField(max_length=70, unique=True)
    created_on=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_post')
    content=models.TextField()
    updated_on=models.DateTimeField(auto_now=True)
    status=models.IntegerField(choices=STATUS, default=0)

    class meta:
        oredreing=['_created_on']

    def __str__(self):
        return self.title    