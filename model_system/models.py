from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE )

    def __str__(self):
        return f"{self.name}:({self.subject.name})"

class Class(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Students(models.Model):
    name = models.CharField(max_length=100)
    class_group = models.ForeignKey(Class,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}:({self.class_group.name})"
    

class Schedule(models.Model):
    DAY_OF_WEEK = [
        ("Mon","Понеділок"),
        ("Tue","Вівторок"),
        ("Web","Середа"),
        ("Thu","Четверг"),
        ("Fri","Пятниця"),
    ]

    day_of_week = models.CharField(max_length=10,choices=DAY_OF_WEEK)
    start_lessons = models.TimeField()
    end_lessons = models.TimeField()
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    school_class = models.ForeignKey(Class,on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)

class Grade(models.Model):
    grade = models.IntegerField()
    data = models.DateField()
    student = models.ForeignKey(Students,on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)