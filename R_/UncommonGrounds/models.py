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

    # NEED CONTRIBUTOR
    # contributor = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)

    description = models.TextField(max_length=1000, help_text="Brief description of location")
    tags = models.ManyToManyField(Tag)
    RATING = (
        (0, ' '),
        (1, '*'),
        (2, '**'),
        (3, '***'),
        (4, '****'),
        (5, '*****'),
    )
    ratings = models.IntegerField(choices=RATING, blank=True, default=' ')
    popularity = models.IntegerField()
    added = models.DateTimeField(auto_now_add=True)
    comments = models.ForeignKey('Comment', related_name="loc_comments", on_delete=models.SET_NULL, null=True) 
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
    user_since = models.DateTimeField(auto_now_add=True)
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
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True) 
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