from django.db import models
from django.contrib.auth.models import User

# Create your models here.
COUNTY=(
    ('Nairobi', "Nairobi"),
    ('Nakuru', "Nakuru"),
    ('Uasin-gishu', "Uasin-gishu"),
    ('Ravine', "Ravine"),
    ('Kisumu', "Kisumu"),
    ('Wajir', "Wajir"),
    ('Kajiado', "Kajiado"),
    ('Kiambu', "Kiambu"),
    ('Elgeyo-marakwet', "Elgeyo-marakwet"),
    ('Nandi', "Nandi"),
    ('Kericho', "Kericho"),
    ('Bomet', "Bomet"),
    ('Thika', "Thika"),
    ('Embakasi', "Embakasi")
)

class Veterinary(models.Model):
    name= models.CharField(max_length=50)
    email=models.EmailField()
    county=models.CharField(choices=COUNTY,max_length=50)
    idNumber=models.IntegerField()
    phoneNumber=models.IntegerField()

    def __str__(self):
        return self.name
    
    # def save(self):
    #     return self.save()
    
    # def delete(self):
    #     return self.delete()