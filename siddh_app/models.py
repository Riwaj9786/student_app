from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.
class Faculty(models.Model):
    faculty_id = models.CharField(max_length=6)
    faculty_name = models.CharField(max_length=70)

    def __str__(self):
        return self.faculty_name



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

    batch_year = models.CharField(max_length=4, validators=[MinLengthValidator(4), MaxLengthValidator(4)])
    first_name = models.CharField(max_length=40)
    middle_name = models.CharField(max_length=40, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    do_birth = models.DateField(auto_now_add=True)
    email_add = models.EmailField(max_length=254)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    semester = models.CharField(max_length=4, choices=SEMESTER_CHOICES)

    def __str__(self):
        return self.first_name
    

class Registration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    registration_number = models.CharField(max_length=30, unique=True)

    def save(self, *args, **kwargs):
        if not self.registration_number:

            # Get the count of existing registrations for the same faculty and batch year
            count = Registration.objects.filter(student__faculty=self.student.faculty, student__batch_year=self.student.batch_year).count() + 1

            # Generate registration number based on faculty code, batch year, and alphabetical character
            self.registration_number = f"{self.student.batch_year}-1-07-{count}"

        super(Registration, self).save(*args, **kwargs)

    def __str__(self):
        return self.student.first_name
    