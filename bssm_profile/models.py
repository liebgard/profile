from django.db import models
from django.utils import timezone


class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category

class Project(models.Model):
    title = models.CharField(max_length=100)
    task = models.CharField(max_length=100)
    description= models.TextField()
    period_from = models.DateTimeField(default=timezone.now)
    period_to = models.DateTimeField(default=timezone.now)
    client = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Skill(models.Model):
    skill = models.CharField(max_length=300)
    project = models.ManyToManyField(Project)

    def __str__(self):
        return self.skill

class Tool(models.Model):
    tool = models.CharField(max_length=100)
    project = models.ManyToManyField(Project)

    def __str__(self):
        return self.tool
