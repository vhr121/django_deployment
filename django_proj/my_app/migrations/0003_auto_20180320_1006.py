# Generated by Django 2.0.2 on 2018-03-20 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_auto_20180320_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='contact_num',
            field=models.CharField(default='Nil', max_length=12),
        ),
    ]
