from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User


class Member(models.Model):
    First_name = models.CharField(max_length=255, null=False)
    Middle_name = models.CharField(max_length=255, null=True, blank=True)
    Last_name = models.CharField(max_length=255, null=False)
    Title = models.CharField(max_length=5)
    Fathers_name = models.CharField(max_length=255)
    Mothers_name = models.CharField(max_length=255)
    Spouse_name = models.CharField(max_length=255, null=True, blank=True)
    Mobile_number1 = models.BigIntegerField(primary_key=True)
    Mobile_number2 = models.BigIntegerField(null=True, blank=True)
    Date_of_birth = models.DateField()
    Gender = models.CharField(max_length=255)  # Removed choices
    Blood_group = models.CharField(max_length=3)  # Removed choices
    Email_id = models.EmailField(max_length=150)
    Door_number = models.CharField(max_length=250)
    Street_name = models.CharField(max_length=250)
    Area = models.CharField(max_length=250)
    District = models.CharField(max_length=250)
    City = models.CharField(max_length=200)
    state = models.CharField(max_length=250)
    Country = models.CharField(max_length=250)
    pin_code = models.IntegerField(null=True)
    Highest_Qualification = models.CharField(max_length=100, null=False)
    Institute = models.CharField(max_length=100, null=False)
    Stream = models.CharField(max_length=100, null=False)
    Passed_out_year = models.IntegerField()
    skills = models.CharField(max_length=250)
    Job_category = models.CharField(max_length=250)
    Company_Name = models.CharField(max_length=250)
    Company_Current_location = models.CharField(max_length=250)
    Job_Position = models.CharField(max_length=250)
    Annual_income = models.CharField(max_length=1000)
    published_date = models.DateField(auto_now=True)

    class Meta:
        db_table = 'new_detail'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    member_id = models.CharField(max_length=10, unique=True)
    class Meta:
        db_table = 'profile'

    def _str_(self):
        return f"{self.user.username} - {self.member_id}"