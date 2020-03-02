from django.db import models
from django.utils.translation import gettext_lazy as lazy

from datetime import datetime

"""
Person class have a name, gender, date of birth, and a derived property age
"""


class Person(models.Model):
    class PersonGender(models.TextChoices):
        MALE = 'M', lazy('Male')
        FEMALE = 'F', lazy('Female')

    person_name = models.CharField(max_length=128, verbose_name="Name")
    person_gender = models.CharField(
        max_length=1,
        choices=PersonGender.choices,
        verbose_name="Gender"
    )
    person_dob = models.DateField(
        verbose_name="Date of birth"
    )
    person_register = models.DateTimeField(
        null=True,
        blank=True,
        auto_now=True,
        verbose_name="Registration timestamp"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return f"{self.person_name}"

    def show_person_dob(self):
        return self.person_dob.strftime('%B %d, %Y')

    def show_person_register(self):
        return self.person_register.strftime('%c')

    def calc_person_age(self):
        """
        Calculates and sets the person age based upon defined timezone
        """
        if self.person_dob is not None:
            current = datetime.now()
            age = current.year - self.person_dob.year

            # Birthday has not been celebrated yet remove 1 year from pre-calculated age
            if self.person_dob.month > current.month:
                age -= 1
            # However it could be that its the birth month but birth day is not today or been passed
            elif self.person_dob.month == current.month:
                if self.person_dob.day != current.day:
                    age -= 1

            self.person_age = age
        return age

    show_person_dob.short_description = "Date of birth"
    show_person_register.short_description = "Timestamp (UTC)"
    calc_person_age.short_description = "Age"


"""
School that a Teacher or Student belongs to
"""


class Schools(models.TextChoices):
    SED = 'SED', lazy('Education')
    SOE = 'SOE', lazy('Engineering')
    SAS = 'SAS', lazy('Arts and Sciences')
    SLG = 'SLG', lazy('Law and Governance')
    SBE = 'SBE', lazy('Business and Economics')
    SHP = 'SHCP', lazy('Healthcare Professions')
    SAFAD = 'SAFAD', lazy('Architecture, Fine Arts and Design')


"""
Teacher teaches Students in Courses
"""


class Teacher(Person, models.Model):
    teacher_school = models.CharField(
        max_length=5,
        choices=Schools.choices,
        verbose_name="School"
    )

    def __str__(self):
        return f"{super().__str__} | {self.teacher_school.label}"


"""
Student may belong in a Course taught by a Teacher
"""


class Student(Person, models.Model):
    pass


"""
Course is taught by a Teacher and attended by Students
"""


class Course(models.Model):
    course_code = models.CharField(
        max_length=32,
        verbose_name="Course code"
    )
    course_school = models.CharField(
        max_length=5,
        choices=Schools.choices,
        verbose_name="School"
    )
    course_enrollees = models.ForeignKey(
        Student,
        verbose_name="Course enrollees",
        on_delete=models.CASCADE
    )
    course_teacher = models.OneToOneField(
        Teacher,
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name="Course teacher"
    )

    def __str__(self):
        return f"{super().__str__} | {self.course_code} {self.course_school.label} "
