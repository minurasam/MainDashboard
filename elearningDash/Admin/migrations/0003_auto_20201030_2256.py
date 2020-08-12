# Generated by Django 3.0.7 on 2020-10-30 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0002_course_course_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='level',
            field=models.CharField(choices=[(1, 'Foundation Level'), (2, 'Operational Level'), (3, 'Management Level'), (4, 'Strategic Level')], max_length=100),
        ),
    ]
