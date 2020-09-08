from django.db import models

# Create your models here.
class Student(models.Model):
    cima_ID = models.CharField(max_length=10, null=True)
    email = models.CharField(max_length=200, null=True)
    NIC = models.IntegerField(null=True)
    first_Name = models.CharField(max_length=200, null=True)
    last_Name = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)

class Course(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80, blank=True, null=True)
    course_describtion = models.TextField(blank=True, null=True)
    faculty = models.ForeignKey('Faculty', models.DO_NOTHING, db_column='faculty', blank=True, null=True)
    category = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course'
    
    def __str__(self):
        return f'Course {self.id} | Name: {self.name}'


class Category(models.Model):
    name = models.CharField(max_length=80, blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, db_column='parent', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'

    def __str__(self):
        return f'Category {self.name}'

class Subject(models.Model):
    
    name = models.CharField(max_length=80, blank=True, null=True)
    category = models.ForeignKey(Category, models.DO_NOTHING, db_column='category', blank=True, null=True)
    thumb = models.CharField(max_length=100, blank=True, null=True)
    pic = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subject'

    def __str__(self):
        return f'Subject {self.id} | Name: {self.name}'