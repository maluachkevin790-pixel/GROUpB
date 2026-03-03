from django.db import models

# Create your models here.
class Student(models.Model):
    image = models.ImageField(upload_to='students/', null=True, blank=True)
    name = models.CharField(max_length=20)
    course = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField()
    gender = models.CharField(
        max_length=20,
        choices=[
            ('Male', 'Male'),
            ('Female', 'Female'),
        ],
        default='Male',
    )
    date = models.DateField(null=True)



    def __str__(self):
        return self.name

from django.db import models

class Exam(models.Model):
    name = models.CharField(max_length=20)
    exam_code = models.CharField(max_length=50, unique=True)
    date = models.DateField()

    def __str__(self):
        return f"{self.name} ({self.exam_code})"
