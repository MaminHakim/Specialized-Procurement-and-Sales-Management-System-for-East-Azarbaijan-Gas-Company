# Generated by Django 2.2.4 on 2019-08-04 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taghaza', '0004_auto_20190803_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taghaza',
            name='tarikh',
            field=models.DateField(verbose_name='تاریخ تقاضا'),
        ),
    ]