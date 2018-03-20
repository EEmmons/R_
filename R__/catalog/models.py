from django.db import models

# Create your models here.
class Tag(models.Model):
    
    tag_name = models.CharField(max_length = 100)

    def __str__(self):
        
        return self.tag_name

class Location(models.Model):
    """
    Model representing a location.
    """

    name = models.CharField(max_length=100, help_text="Enter the name of location")
    """GPS_coordinates = """
    description = models.TextField(max_length=1000, help_text="Brief description of location")
    tags = models.ManyToManyField(Tag)
    ratings = models.FloatField()
    popularity = models.IntegerField()
    comments = models.TextField(max_length=1000)
    image = models.ImageField(upload_to = 'location_images/',default = 'pic_folder/None/no-img.jpg')
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name


class User(models.Model):
    """
    Model representing a User.
    """
    username = models.CharField(max_length=50, help_text="Enter username")
    password = models.CharField(max_length=50, help_text="Enter password")
    user_tags = models.ManyToManyField(Tag)
    favorites = models.ManyToManyField(Location)
    location = models.CharField(max_length=100, help_text="location")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.username
