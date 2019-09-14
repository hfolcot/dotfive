from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, blank=False)
    parent = models.ForeignKey('self', null=True, on_delete=models.PROTECT)
    is_top_level = models.BooleanField(default=True)

    def __str__(self):
        return self.name