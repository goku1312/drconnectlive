# Generated by Django 5.0.2 on 2024-03-19 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_doctorregister_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorregister',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
