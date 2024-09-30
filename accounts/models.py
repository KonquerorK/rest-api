from django.db import models

class Property(models.Model):
    dimensions = models.CharField(max_length=100)
    construction_year = models.IntegerField()
    details = models.TextField()
    photo = models.ImageField(upload_to='property_photos/', null=True, blank=True)

    def __str__(self):
        return f"Property {self.id} - {self.dimensions}"
