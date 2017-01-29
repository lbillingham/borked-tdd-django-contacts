"""models for organisation etc. """
from django.db import models

class Organisation(models.Model):
    _max_name_len = 255
    name = models.CharField(max_length=_max_name_len, default='', null=False)
    email = models.EmailField(default='', null=False)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        """string representation"""
        return self.name
