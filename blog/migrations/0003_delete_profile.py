# Generated by Django 2.2.3 on 2019-07-26 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
