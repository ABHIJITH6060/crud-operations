from django.db import models

# Create your models here.

class furniture(models.Model):
    furniture_types = (
        ('wood', 'wood'),
        ('plastic', 'plastic'),
        ('steel', 'steel'),
    )

    Name =models.CharField(max_length=20)
    Price =models.IntegerField()
    Types =models.CharField(max_length=20,choices=furniture_types)
    Details =models.TextField()
