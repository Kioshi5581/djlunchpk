from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from phone_field import PhoneField
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from rest_framework.authtoken.models import Token
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  

# Create your models here.


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "/apioverview/password_reset/confirm/"

    send_mail(
        # title:
        "Rest your password - {title}".format(title="Lunch.pk"),
        # message:
        f"Your Token: {reset_password_token.key} \n Url: {email_plaintext_message} ",
        # from:
        "lunchpk@lunch.pk",
        # to:
        [reset_password_token.user.email]
    )


class Deals(models.Model):
    name = models.CharField(max_length=220)
    deal_img = models.ImageField(upload_to='media/', default='media/Capture.PNG', blank=True)
    persons = models.IntegerField()
    details = models.CharField(max_length=500)
    price = models.IntegerField()
    price3 = models.IntegerField(default=1250)
    

    
    def __str__(self):
        return f'{self.name}'

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Frozen(models.Model):
    name = models.CharField(max_length=220)
    frzn_img = models.ImageField(upload_to='media/', default='media/Capture.PNG', blank=True)
    persons = models.IntegerField()
    pieces = models.IntegerField()
    price = models.IntegerField()


    
    def __str__(self):
        return f'{self.name}'
    

class foodlancer(models.Model):
    Your_Name = models.CharField(max_length=50)
    Kitchen_Name = models.CharField(max_length=50)
    Email_Address = models.EmailField(max_length=50)
    Street_Address = models.CharField(max_length=50)
    City = models.CharField(max_length=5)
    phone = PhoneNumberField(unique=True)
    
    def __str__(self):
        return f'{self.Your_Name}'



CITIES =(
    ("Islamabad", "Islamabad"),
    ("karachi", "Karachi"),
    ("lahore", "Lahore"),
    ("rawalpindi", "Rawalpindi"),
    ("other", "Other"),
)


TIME =(
    ("lunch", "Lunch"),
    ("dinner", "Dinner"),
    ("other", "Other"),
)



PAKAGES =(
    ("Kari", "Kari Pakora"),
    ("Keema", "Aloo Keema"),
    ("Handi", "Boneless Handi"),
    ("Pulao", "Chicken Pulao"),
    ("Macaroni", "Chicken Macaroni"),
    ("Korma", "Chicken Korma"),
    ("Jalfrezi", "Chicken Jalfrezi with Rice"),
    ("Karahi", "Mutton Karahi"),
    ("Tandoori", "Fried Rice w Tandoori"),
    ("Chowmein", "Chicken Chow mein"),
    ("Chicken", "Chicken Leg Piece"),
    ("Kebab", "Seekh Kebab"),
    ("Samosa", "Chicken Chinese Samosa"),
    ("Rolls", "Chicken Chinese Rolls"),
    ("Nuggets", "Chicken Nuggets"),
    ("BreadRolls", "Chicken Bread Rolls"),
    ("ShamiKebab", "Chicken Shami Kebab"),
    ("ChickenBalls", "Aloo Chicken Balls"),
    ("Economy", "Economy Menu"),
    ("Mazedar", "Mazedar Menu"),
    ("Executive", "Executive Menu"),
    ("WeightLoss", "Weight Loss Diet Plan"),
    ("TwoTime", "2 Time Meal"),
    ("Corporate", "Corporate Menu"),
    ("HighBloodPressure", "High Blood Pressure Menu"),
)



class Customers(models.Model):
    Your_Name = models.CharField(max_length=220)
    Email_Address = models.EmailField(max_length=220)
    Profession = models.CharField(max_length=220)
    phone = PhoneNumberField(unique=True)
    No_of_Persons = models.IntegerField()
    Packages = models.CharField(choices=PAKAGES, max_length=100)
    Address = models.CharField(max_length=220)
    City = models.CharField(choices=CITIES, max_length=10)
    Time = models.CharField(choices=TIME, max_length=10)
    Message = models.TextField()
    
    def __str__(self):
        return f'{self.Your_Name}'

class Contact(models.Model):
    Your_Name = models.CharField(max_length=250)
    Email_Address = models.EmailField(max_length=220)
    phone = PhoneNumberField(unique=True)
    Message = models.TextField()
    
    def __str__(self):
        return f'{self.Your_Name}'



class MonthlyPackage(models.Model):
    package_name = models.CharField(max_length=220)
    package_desc = models.CharField(max_length=220)
    package_price = models.IntegerField()
    # Week on
    week_1_mon = models.CharField(max_length=220)
    week_1_tue = models.CharField(max_length=220)
    week_1_wed = models.CharField(max_length=220)
    week_1_thu = models.CharField(max_length=220)
    week_1_fri = models.CharField(max_length=220)
    week_1_sat = models.CharField(max_length=220)
    # Week 2
    week_2_mon = models.CharField(max_length=220)
    week_2_tue = models.CharField(max_length=220)
    week_2_wed = models.CharField(max_length=220)
    week_2_thu = models.CharField(max_length=220)
    week_2_fri = models.CharField(max_length=220)
    week_2_sat = models.CharField(max_length=220)
    # week 3
    week_3_mon = models.CharField(max_length=220)
    week_3_tue = models.CharField(max_length=220)
    week_3_wed = models.CharField(max_length=220)
    week_3_thu = models.CharField(max_length=220)
    week_3_fri = models.CharField(max_length=220)
    week_3_sat = models.CharField(max_length=220)
    # week 4
    week_4_mon = models.CharField(max_length=220)
    week_4_tue = models.CharField(max_length=220)
    week_4_wed = models.CharField(max_length=220)
    week_4_thu = models.CharField(max_length=220)
    week_4_fri = models.CharField(max_length=220)
    week_4_sat = models.CharField(max_length=220)
 
    
    def __str__(self):
        return f'{self.package_name}'


class djuser(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_added = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
