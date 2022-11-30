# Generated by Django 3.2.12 on 2022-11-30 16:52

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iin_number', models.CharField(max_length=12, verbose_name='IIN Number')),
                ('id_number', models.CharField(max_length=20, verbose_name='ID Number')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('surname', models.CharField(max_length=128, verbose_name='Surname')),
                ('middle_name', models.CharField(blank=True, max_length=128, verbose_name='Middle Name')),
                ('blood_group', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(4), django.core.validators.MinValueValidator(1)], verbose_name='Blood Group')),
                ('emergency_contact_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='KZ', verbose_name='Phone Number')),
                ('email', models.EmailField(blank=True, max_length=256, null=True, unique=True, verbose_name='Email Address')),
                ('address', models.CharField(max_length=256, verbose_name='Address')),
                ('marital_status', models.CharField(choices=[('married', 'Married'), ('single', 'Single'), ('divorced', 'Divorced')], default='single', max_length=126, verbose_name='Marital Status')),
                ('registration_date', models.DateField(auto_now=True, verbose_name='Registration Date')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='patient', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Patient',
                'verbose_name_plural': 'Patients',
                'db_table': 'patients',
            },
        ),
    ]