from django.db import models

class Person(models.Model):
    first_name      = models.CharField(blank=True,null=True,max_length=255)
    last_name       = models.CharField(blank=True,null=True,max_length=255)
    birthday        = models.DateField(blank=True,null=True)
    phone_number    = models.CharField(blank=True,null=True,max_length=10)
    city            = models.CharField(blank=True,null=True,max_length=100)
    provence        = models.CharField(blank=True,null=True,max_length=100)
    commune         = models.CharField(blank=True,null=True,max_length=100)
    blood_type      = models.CharField(blank=True,null=True,max_length=5)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
