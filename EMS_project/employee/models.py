from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    email = models.EmailField(blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return '{}'.format(self.name)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)