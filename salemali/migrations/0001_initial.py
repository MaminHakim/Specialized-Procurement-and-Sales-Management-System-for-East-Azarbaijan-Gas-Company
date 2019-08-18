# Generated by Django 2.2.3 on 2019-07-19 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Salemali',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sal', models.IntegerField(verbose_name='سال')),
                ('arzeshe_afzude', models.IntegerField(default=0, verbose_name='درصد ارزش افزوده')),
                ('nerkhe_tafkik', models.IntegerField(verbose_name='نرخ تفکیک معامله ها ')),
            ],
            options={
                'verbose_name': 'سال مالی',
                'verbose_name_plural': 'سال\u200cهای مالی',
            },
        ),
    ]