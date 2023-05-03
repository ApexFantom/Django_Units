from django.db import models

class Students(models.Model):
    first_name = models.CharField(max_length=256)
    second_name = models.CharField(max_length=256)

    def __str__(self):
        return self.second_name

