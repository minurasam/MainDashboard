# Generated by Django 3.1 on 2020-09-14 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acc_type', models.IntegerField(choices=[(1, 'Lecturer'), (2, 'Student')], default=2)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cima_ID', models.CharField(max_length=10, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('first_Name', models.CharField(max_length=200, null=True)),
                ('last_Name', models.CharField(max_length=200, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.account')),
            ],
        ),
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lec_NIC', models.CharField(max_length=10)),
                ('first_Name', models.CharField(max_length=200, null=True)),
                ('last_Name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.account')),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=10)),
                ('course_name', models.CharField(max_length=100)),
                ('course_level', models.IntegerField(choices=[(1, 'Certificate level'), (2, 'Operational Level'), (3, 'Management Level'), (4, 'Strategic Level')])),
                ('lecturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.lecturer')),
                ('student', models.ManyToManyField(to='Admin.Student')),
            ],
        ),
    ]
