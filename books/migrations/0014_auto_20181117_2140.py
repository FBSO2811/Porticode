# Generated by Django 2.1.3 on 2018-11-17 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0013_auto_20181117_1852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='genre',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('m', 'Masculine'), ('f', 'Feminine'), ('o', 'Other')], max_length=1, null=True),
        ),
    ]
