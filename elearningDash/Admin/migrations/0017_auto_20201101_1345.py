# Generated by Django 3.0.7 on 2020-11-01 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0016_auto_20201101_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='Admin.Module'),
        ),
    ]
