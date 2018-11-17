# Generated by Django 2.1.3 on 2018-11-10 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20181110_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='condition_choices',
            field=models.CharField(choices=[('NE', 'New - Never Used'), ('Used', 'Used but seems still new'), ('Used', 'Used but in good conditions'), ('Used', 'Used and you can see it')], max_length=100),
        ),
    ]
