from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class Faculty(models.Model):
    faculty_id = models.CharField(max_length=6, unique=True)
    faculty_name = models.CharField(max_length=70)

    def __str__(self):
        return self.faculty_id



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
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    semester = models.CharField(max_length=4, choices=SEMESTER_CHOICES)

    def save(self, *args, **kwargs):
        if not self.registration_number:

            # Generate registration number based on faculty code, batch year, and student count
            count = Student.objects.filter(faculty=self.faculty, batch_year=self.batch_year).count() + 1
            registration_number = f"{self.batch_year}-1-{self.faculty.pk}-{count}"
            self.registration_number = slugify(registration_number)  # Generate a slug from the registration number
        
        super().save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse("siddh_app:studentrecord")


    def __str__(self):
        return self.first_name
    


    