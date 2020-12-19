from django.db import models

# Create your models here.


class List(models.Model):
    master = models.ForeignKey(
        'self', blank=True, null=True, related_name='unit_parent', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default='')
    text = models.TextField(default='')

    def __str__(self):
        return self.name
