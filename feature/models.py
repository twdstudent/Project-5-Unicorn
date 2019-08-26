from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Feature(models.Model):
    """
    A single feature posting
    """
    title = models.CharField(max_length=254, default='')
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    owner = models.ForeignKey(User, related_name='feature', null=False,
                              default=1, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.title