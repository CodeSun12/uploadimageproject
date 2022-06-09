from django.db import models


# Create your models here.
class Profile(models.Model):
    def nameFile(self, filename):
        return '/'.join(['images', str(self.name), filename])
    name = models.CharField(max_length=50),
    image = models.ImageField(upload_to=nameFile, blank=True)
