# Generated by Django 2.2.3 on 2019-07-19 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kala',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sharh', models.CharField(max_length=100, verbose_name='شرح')),
                ('vahede_andazegiri', models.CharField(max_length=15, verbose_name='واحد اندازه گیری')),
            ],
            options={
                'verbose_name': 'کالا',
                'verbose_name_plural': 'کالا ها',
            },
        ),
    ]
