from django.db import models
from passlib.hash import pbkdf2_sha256

choices = (
    ('Active', 'Active'),
    ('Inactive', 'Inactive'),
)


# Create your models here.
class Role(models.Model):
    role_name = models.CharField(max_length=30)

    def __str__(self):
        return self.role_name


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    password = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    role = models.ForeignKey(Role, on_delete=models.CharField)
    status = models.CharField(max_length=20, choices=choices, default=0)

    def __str__(self):
        return self.name

    def verify_password(self, raw_password):
        return pbkdf2_sha256.verify(raw_password, self.password)
