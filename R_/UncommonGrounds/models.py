from django.db import models
from django.utils.timezone import now

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
    # comments = models.ForeignKey('Comment', on_delete=models.SET_NULL, null=True) 
    image = models.ImageField(upload_to = 'location_images/')

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
    favorites = models.ManyToManyField(Location, related_name = "faves")
    # location = models.CharField(max_length=100, help_text="location")
    locations = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True) 

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.username


class Comment(models.Model):
    """
    Model representing a comment.
    """
    author = models.ForeignKey('User', on_delete=models.SET_NULL, null=True) 
    text = models.TextField(max_length=500)
    created_date = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()
        """
        This will be used to moderate comments and make sure only valid users can comment
        """

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.text