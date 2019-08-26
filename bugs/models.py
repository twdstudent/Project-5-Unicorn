from django.db import models
from django.utils import timezone

# Create your models here.
"""
A single bug posting
"""

class Bugs(models.Model):
    STATUS_CHOICES = (
            ('todo', 'To do'),
            ('doing', 'Doing'),
            ('done', "Done"),
        )
    status = models.CharField(max_length=5, choices=STATUS_CHOICES, default="todo")
    upvotes = models.IntegerField(default=0)
    title = models.CharField(max_length=254, default='')
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to="img", blank=True, null=True)

    def __str__(self):
        return self.title


