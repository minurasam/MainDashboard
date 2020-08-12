# Generated by Django 3.0.7 on 2020-10-30 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0005_auto_20201030_2301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='module',
            name='lecturer',
        ),
        migrations.AddField(
            model_name='course',
            name='lecturer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin.Lecturer'),
        ),
    ]
