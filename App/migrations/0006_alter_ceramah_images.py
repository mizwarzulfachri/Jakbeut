# Generated by Django 4.0.3 on 2022-05-16 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_alter_ceramah_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ceramah',
            name='Images',
            field=models.ImageField(upload_to='static/images/'),
        ),
    ]
