# Generated by Django 2.0.1 on 2018-02-17 02:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('roomrentalscn', '0002_auto_20180216_0147'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomRentalCn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('streetname', models.CharField(blank=True, max_length=120, null=True)),
                ('postalcode', models.CharField(blank=True, max_length=120, null=True)),
                ('block', models.CharField(blank=True, max_length=120, null=True)),
                ('roomtype', models.CharField(blank=True, max_length=120, null=True)),
                ('price', models.CharField(blank=True, max_length=120, null=True)),
                ('public', models.BooleanField(default=True)),
                ('appointmentdate', models.DateField(blank=True, max_length=120, null=True)),
                ('appointmenttime', models.TimeField(blank=True, max_length=120, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-updated', 'timestamp'],
            },
        ),
    ]
