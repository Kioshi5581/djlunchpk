# Generated by Django 3.2.9 on 2022-03-25 15:04

from django.db import migrations, models
import django.db.models.deletion
import lunchpkapp.models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Your_Name', models.CharField(max_length=250)),
                ('Email_Address', models.EmailField(max_length=220)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('Message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Your_Name', models.CharField(max_length=220)),
                ('Email_Address', models.EmailField(max_length=220)),
                ('Profession', models.CharField(max_length=220)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('No_of_Persons', models.IntegerField()),
                ('Packages', models.CharField(choices=[('Kari', 'Kari Pakora'), ('Keema', 'Aloo Keema'), ('Handi', 'Boneless Handi'), ('Pulao', 'Chicken Pulao'), ('Macaroni', 'Chicken Macaroni'), ('Korma', 'Chicken Korma'), ('Jalfrezi', 'Chicken Jalfrezi with Rice'), ('Karahi', 'Mutton Karahi'), ('Tandoori', 'Fried Rice w Tandoori'), ('Chowmein', 'Chicken Chow mein'), ('Chicken', 'Chicken Leg Piece'), ('Kebab', 'Seekh Kebab'), ('Samosa', 'Chicken Chinese Samosa'), ('Rolls', 'Chicken Chinese Rolls'), ('Nuggets', 'Chicken Nuggets'), ('BreadRolls', 'Chicken Bread Rolls'), ('ShamiKebab', 'Chicken Shami Kebab'), ('ChickenBalls', 'Aloo Chicken Balls'), ('Economy', 'Economy Menu'), ('Mazedar', 'Mazedar Menu'), ('Executive', 'Executive Menu'), ('WeightLoss', 'Weight Loss Diet Plan'), ('TwoTime', '2 Time Meal'), ('Corporate', 'Corporate Menu'), ('HighBloodPressure', 'High Blood Pressure Menu')], max_length=100)),
                ('Address', models.CharField(max_length=220)),
                ('City', models.CharField(choices=[('Islamabad', 'Islamabad'), ('karachi', 'Karachi'), ('lahore', 'Lahore'), ('rawalpindi', 'Rawalpindi'), ('other', 'Other')], max_length=10)),
                ('Time', models.CharField(choices=[('lunch', 'Lunch'), ('dinner', 'Dinner'), ('other', 'Other')], max_length=10)),
                ('Date', models.DateTimeField()),
                ('Message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Deals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=220)),
                ('deal_img', models.ImageField(blank=True, default='media/Capture.PNG', upload_to='media/')),
                ('persons', models.IntegerField()),
                ('details', models.CharField(max_length=500)),
                ('price', models.IntegerField()),
                ('price3', models.IntegerField(default=1250)),
            ],
        ),
        migrations.CreateModel(
            name='djuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='foodlancer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Your_Name', models.CharField(max_length=50)),
                ('Kitchen_Name', models.CharField(max_length=50)),
                ('Email_Address', models.EmailField(max_length=50)),
                ('Street_Address', models.CharField(max_length=50)),
                ('City', models.CharField(max_length=5)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Frozen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=220)),
                ('frzn_img', models.ImageField(blank=True, default='media/Capture.PNG', upload_to='media/')),
                ('persons', models.IntegerField()),
                ('pieces', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MonthlyPackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(max_length=220)),
                ('package_desc', models.CharField(max_length=220)),
                ('package_price', models.IntegerField()),
                ('week_1_mon', models.CharField(max_length=220)),
                ('week_1_tue', models.CharField(max_length=220)),
                ('week_1_wed', models.CharField(max_length=220)),
                ('week_1_thu', models.CharField(max_length=220)),
                ('week_1_fri', models.CharField(max_length=220)),
                ('week_1_sat', models.CharField(max_length=220)),
                ('week_2_mon', models.CharField(max_length=220)),
                ('week_2_tue', models.CharField(max_length=220)),
                ('week_2_wed', models.CharField(max_length=220)),
                ('week_2_thu', models.CharField(max_length=220)),
                ('week_2_fri', models.CharField(max_length=220)),
                ('week_2_sat', models.CharField(max_length=220)),
                ('week_3_mon', models.CharField(max_length=220)),
                ('week_3_tue', models.CharField(max_length=220)),
                ('week_3_wed', models.CharField(max_length=220)),
                ('week_3_thu', models.CharField(max_length=220)),
                ('week_3_fri', models.CharField(max_length=220)),
                ('week_3_sat', models.CharField(max_length=220)),
                ('week_4_mon', models.CharField(max_length=220)),
                ('week_4_tue', models.CharField(max_length=220)),
                ('week_4_wed', models.CharField(max_length=220)),
                ('week_4_thu', models.CharField(max_length=220)),
                ('week_4_fri', models.CharField(max_length=220)),
                ('week_4_sat', models.CharField(max_length=220)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Invoice_Number', models.CharField(default=lunchpkapp.models.inv_num, max_length=10)),
                ('Recurring', models.CharField(choices=[('No', 'No'), ('1 Month', 'Every 1 Month'), ('2 Month', 'Every 2 Month'), ('3 Month', 'Every 3 Month'), ('4 Month', 'Every 4 Month'), ('5 Month', 'Every 5 Month'), ('6 Month', 'Every 6 Month'), ('7 Month', 'Every 7 Month'), ('9 Month', 'Every 9 Month'), ('10 Month', 'Every 10 Month'), ('11 Month', 'Every 11 Month'), ('12 Month', 'Every 12 Month')], max_length=12)),
                ('Invoice_date', models.DateField()),
                ('Due_date', models.DateField()),
                ('Packages', models.CharField(choices=[('Kari', 'Kari Pakora'), ('Keema', 'Aloo Keema'), ('Handi', 'Boneless Handi'), ('Pulao', 'Chicken Pulao'), ('Macaroni', 'Chicken Macaroni'), ('Korma', 'Chicken Korma'), ('Jalfrezi', 'Chicken Jalfrezi with Rice'), ('Karahi', 'Mutton Karahi'), ('Tandoori', 'Fried Rice w Tandoori'), ('Chowmein', 'Chicken Chow mein'), ('Chicken', 'Chicken Leg Piece'), ('Kebab', 'Seekh Kebab'), ('Samosa', 'Chicken Chinese Samosa'), ('Rolls', 'Chicken Chinese Rolls'), ('Nuggets', 'Chicken Nuggets'), ('BreadRolls', 'Chicken Bread Rolls'), ('ShamiKebab', 'Chicken Shami Kebab'), ('ChickenBalls', 'Aloo Chicken Balls'), ('Economy', 'Economy Menu'), ('Mazedar', 'Mazedar Menu'), ('Executive', 'Executive Menu'), ('WeightLoss', 'Weight Loss Diet Plan'), ('TwoTime', '2 Time Meal'), ('Corporate', 'Corporate Menu'), ('HighBloodPressure', 'High Blood Pressure Menu')], max_length=100)),
                ('Package_name', models.CharField(max_length=50)),
                ('Package_description', models.TextField()),
                ('Package_Quantity', models.IntegerField()),
                ('Package_Price', models.IntegerField()),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lunchpkapp.customers')),
            ],
        ),
    ]
