# Generated by Django 4.0.3 on 2022-04-03 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('UserID', models.AutoField(primary_key=True, serialize=False)),
                ('UserName', models.CharField(max_length=500)),
                ('UserEmail', models.CharField(max_length=500)),
                ('UserPassword', models.CharField(max_length=500)),
                ('UserPhone', models.IntegerField(max_length=20)),
                ('UserAddress', models.CharField(max_length=500)),
                ('UserCountry', models.CharField(max_length=500)),
                ('JoinedDate', models.DateField()),
            ],
        ),
    ]