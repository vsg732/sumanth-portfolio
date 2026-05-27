from django.db import models

# Create your models here.
# models.py
from django.db import models

class PortfolioData(models.Model):
    actor_name = models.CharField(max_length=100)
    
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    instagram = models.URLField()
    facebook = models.URLField()
    twitter = models.URLField()
    youtube = models.URLField()
    
    background = models.ImageField(upload_to='uploads/')
    about_image = models.ImageField(upload_to='uploads/')
    
    about_description = models.TextField()


class Filmography(models.Model):

    portfolio = models.ForeignKey(
        PortfolioData,
        on_delete=models.CASCADE,
        related_name="films"
    )

    title = models.CharField(max_length=100)

    role = models.CharField(max_length=100)

    year = models.CharField(max_length=10)

    poster = models.ImageField(upload_to='films/')

    trailer = models.URLField(blank=True, null=True)

class Gallery(models.Model):

    portfolio = models.ForeignKey(
        PortfolioData,
        on_delete=models.CASCADE,
        related_name='gallery'
    )

    image = models.ImageField(upload_to='gallery/')

    image_name = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.image_name or "Gallery Image"