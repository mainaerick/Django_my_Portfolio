from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


# # Create your models here.

class About(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    title = models.CharField(max_length=200)

    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True, default="avatar.svg")
    resume = models.FileField(null=True, default="cv.txt")

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    git_repo = models.CharField(max_length=200)
    live_link = models.CharField(max_length=200)
    image = models.ImageField(null=True, default="avatar.svg")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Skill(models.Model):
    title = models.CharField(max_length=200)
    skill_level = models.CharField(max_length=200)
    image = models.ImageField(null=True, default="avatar.svg")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Tool(models.Model):
    title = models.CharField(max_length=200)
    logo = models.ImageField(null=True, default="avatar.svg")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Experience(models.Model):
    duration = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.duration


class Message(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
