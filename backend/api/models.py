from django.db import models
from .enum import NewsTypes
from django.contrib.auth.models import User 

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=10, choices=NewsTypes.choices, default=NewsTypes.INFO)

    def __str__(self):
        return self.title
    
    
class StudyProgram(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Semester(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

class Module(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    study_programs = models.ManyToManyField(StudyProgram, related_name='modules')
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class UserStudyProgram(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    study_program = models.ForeignKey(StudyProgram, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.study_program.name}"
    
class StudentModule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_modules')
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='student_modules')
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('user', 'module')

    def __str__(self):
        return f"{self.user.username} - {self.module.name} ({'Aktiv' if self.is_active else 'Inaktiv'})"
