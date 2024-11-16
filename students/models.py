from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=32, null=False, blank=False)
    age = models.PositiveIntegerField(null=False, blank=False)
    gender = models.CharField(max_length=32, null=False, blank=False)
    profile_image = models.ImageField(upload_to='profiles/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    email = models.EmailField(null=False, blank=False)

    def __str__(self):
        return self.name
