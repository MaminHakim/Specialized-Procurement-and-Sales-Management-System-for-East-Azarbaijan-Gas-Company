# Generated by Django 2.2.4 on 2019-08-12 10:13

from django.db import migrations, models
import taghaza.models


class Migration(migrations.Migration):

    dependencies = [
        ('taghaza', '0016_auto_20190811_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taghaza',
            name='image',
            field=models.ImageField(default='static/pics/no-pic.jpg', upload_to=taghaza.models.Taghaza.user_directory_path, verbose_name='تصویر فرم تقاضای کالا (MT26)'),
        ),
    ]
