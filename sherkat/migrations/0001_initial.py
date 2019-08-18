# Generated by Django 2.2.3 on 2019-07-19 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sherkat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nam', models.CharField(max_length=15, verbose_name='نام شرکت')),
                ('tel', models.IntegerField()),
                ('mob', models.IntegerField()),
            ],
            options={
                'verbose_name': 'شرکت',
                'verbose_name_plural': 'شرکت ها',
            },
        ),
    ]