from django import forms
from .models import *
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class Deals_form(forms.ModelForm):
    class Meta:
        model = Deals
        fields = '__all__'

class FoodlancerRegistration(forms.ModelForm):
    phone = forms.CharField(widget=PhoneNumberPrefixWidget(initial="PK"))

    class Meta:
        model = foodlancer
        fields = ["Your_Name", "Kitchen_Name", "Email_Address", "Street_Address", "City", "phone"]

class Order_Now(forms.ModelForm):
    phone = forms.CharField(widget=PhoneNumberPrefixWidget(initial="PK"))
    class Meta:
        model = Customers
        fields = ["Your_Name", "Email_Address", "phone", "Profession", "Packages", "No_of_Persons", "Address", "Time", "City", "Message"]

class Contact_form(forms.ModelForm):
    phone = forms.CharField(widget=PhoneNumberPrefixWidget(initial="PK"))
    class Meta:
        model = Contact
        fields = ["Your_Name", "Email_Address", "phone", "Message"]

class UserModelForm(forms.ModelForm):
    phone_number = forms.CharField(widget=PhoneNumberPrefixWidget(initial="PK"))
    class Meta:
        model = djuser
        fields = (
            'first_name',
            'last_name',
            'phone_number',
            'email',

        )


