# Generated by Django 2.2.2 on 2019-07-21 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aghlam', '0004_auto_20190721_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aghlam',
            name='sherkat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sherkat.Sherkat', verbose_name='تامین کننده'),
        ),
    ]
