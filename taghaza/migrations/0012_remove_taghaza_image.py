# Generated by Django 2.2.4 on 2019-08-11 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taghaza', '0011_auto_20190811_1036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taghaza',
            name='image',
        ),
    ]