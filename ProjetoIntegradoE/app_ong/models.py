from django.db import models


class Ong(models.Model):
    email = models.CharField(max_length=50, unique=True, null=False, blank=False)
    password = models.CharField(max_length=16, null=False, blank=False)
    name_fantasy = models.CharField(max_length=100, null=False, blank=False)
    name_social = models.CharField(max_length=100, null=False, blank=False)
    cell = models.IntegerField()
    dt_foundation = models.DateTimeField()
    cnpj = models.IntegerField(null=False, blank=False)
    image = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.name_fantasy
