from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now())

#由于版本的原因，此处需要自己添加objects的属性
    objects = models.Manager()
    class Meat:
        ordering = ('-pub_date')

    def __unicode__(self):
        return self.title