from django.db import models
from django.contrib.auth.models import User

class Location(models.Model):
    # one query made by a user into a certain location
    latitude = models.FloatField()
    longitude = models.FloatField()
    radius = models.FloatField()
    name = models.CharField(max_length = 200)
    date = models.DateTimeField('date created')
    latest_data = models.DateTimeField('last time this location was updated')
    user = models.ForeignKey(User)

    def __str__(self):
        return self.name

class Pushpin(models.Model):
    # one piece of information (one tweet, one flickr photo, etc.)
    SOURCES = (
                ("TW", "Twitter"),
                ("FL", "Flickr"),
                ("PI", "Picasa"),
                ("SH", "Shodan"),
                ("YU", "Youtube"),
                ("FB", "Facebook"),
                ("LI", "LinkedIn")
              )
    source = models.CharField(choices=SOURCES, max_length=2)
    date = models.DateTimeField('date published')
    screen_name = models.CharField(max_length=100)
    profile_name = models.CharField(max_length=100)
    profile_url = models.URLField()
    media_url = models.URLField()
    thumb_url = models.URLField()
    message = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    location = models.ForeignKey(Location)

    def __str__(self):
        return "pin by " + self.screen_name + " from " + self.source

class Keys(models.Model):
    # hold's a user's API keys
    flickr_api = models.CharField(max_length = 50, blank=True)
    google_api = models.CharField(max_length = 50, blank=True)
    shodan_api = models.CharField(max_length = 50, blank=True)
    twitter_api = models.CharField(max_length = 50, blank=True)
    twitter_secret = models.CharField(max_length = 50, blank=True)
    linkedin_api = models.CharField(max_length = 50, blank=True)
    linkedin_secret = models.CharField(max_length = 50, blank=True)
    facebook_api = models.CharField(max_length = 50, blank=True)
    facebook_secret = models.CharField(max_length = 50, blank=True)
    facebook_username = models.CharField(max_length = 50, blank=True)
    facebook_password = models.CharField(max_length = 50, blank=True)
    user = models.OneToOneField(User, primary_key=True)

    def __str__(self):
        return self.user + "'s API keys"
