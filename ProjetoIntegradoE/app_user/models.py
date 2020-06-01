from django.db import models


class User(models.Model):
    email = models.CharField(max_length=50, unique=True, null=False, blank=False)
    password = models.CharField(max_length=16, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    cell = models.IntegerField()
    dt_birthday = models.DateTimeField(null=False, blank=False)
    cpf = models.IntegerField(null=False, blank=False)
    image = models.CharField(max_length=50)

    def __str__(self):
        return self.name
