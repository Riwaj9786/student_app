from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class College(models.Model):
    COLLEGE_CHOICES = (
        (1, "Central"),
        (2, "Affiliated"),
    )

    col_id = models.CharField(max_length=12, unique=True)
    college_name = models.CharField(max_length=100)
    college_type = models.PositiveIntegerField(choices= COLLEGE_CHOICES)

    def __str__(self):
        return self.col_id
    


class Faculty(models.Model):
    faculty_id = models.CharField(max_length=6, unique=True)
    faculty_name = models.CharField(max_length=70)

    def __str__(self):
        return self.faculty_id
    


class Course(models.Model):
    course_id = models.CharField(max_length=8, unique=True)
    course_name = models.CharField(max_length=50)

    def __str__(self):
        return self.course_name




class Department(models.Model):
    faculty = models.ForeignKey(Faculty,default=None, on_delete=models.CASCADE)
    depart_id = models.CharField(max_length=12, unique=True)
    depart_name = models.CharField(max_length=35)
    courses = models.ManyToManyField(Course, related_name='departments')

    def __str__(self):
        return self.depart_id
    


class Student(models.Model):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    SEMESTER_CHOICES = (
        ('I', 'I'),
        ('II', 'II'),
        ('III', 'III'),
        ('IV', 'IV'),
        ('V', 'V'),
        ('VI', 'VI'),
        ('VII', 'VII'),
        ('VIII', 'VIII'),
    )

    registration_number = models.CharField(max_length=30, default=None, unique=True, editable=False)
    batch_year = models.CharField(max_length=4, validators=[MinLengthValidator(4), MaxLengthValidator(4)])
    first_name = models.CharField(max_length=40)
    middle_name = models.CharField(max_length=40, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    do_birth = models.DateField()
    email_add = models.EmailField(max_length=254)
    college = models.ForeignKey(College, default=None, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    depart = models.ForeignKey(Department, default=None, on_delete=models.CASCADE)
    semester = models.CharField(max_length=4, choices=SEMESTER_CHOICES)

    def save(self, *args, **kwargs):
        if not self.registration_number:

            # Generate registration number based on faculty code, batch year, and student count
            count = Student.objects.filter(faculty=self.faculty, batch_year=self.batch_year).count() + 1
            registration_number = f"{self.batch_year}-{self.college.college_type}-{self.faculty.pk}-{count}"
            self.registration_number = slugify(registration_number)  # Generate a slug from the registration number
        
        super().save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse("siddh_app:studentrecord")


    def __str__(self):
        return self.first_name
    





    