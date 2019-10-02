from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

"""
A single feature posting
"""

class Feature(models.Model):
    STATUS_CHOICES = (
            ('todo', 'To do'),
            ('doing', 'Doing'),
            ('done', "Done"),
        )
    status = models.CharField(max_length=5, choices=STATUS_CHOICES, default="todo")
    upvotes = models.IntegerField(default=0)
    title = models.CharField(max_length=254, default='')
    content = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, default=10)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    owner = models.ForeignKey(User, related_name='feature', null=False,
                              default=1, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.title