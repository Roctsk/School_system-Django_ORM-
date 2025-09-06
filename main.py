import django_setup
from model_system.models import Subject, Teacher, Class, Students , Schedule ,Grade
from datetime import time

# math = Subject.objects.create(name="Математика")
# english = Subject.objects.create(name="Англійська мова")

# teacher1 = Teacher.objects.create(name = "Ольга" ,surname = "Василівна", subject = math)
# teacher2 = Teacher.objects.create(name = "Микола " ,surname = "Степанович", subject = english)

# class5a = Class.objects.create(name="5-А")
# class6b = Class.objects.create(name="6-Б")

# Students.objects.create(name="Василь Коваль", class_group=class5a)
# Students.objects.create(name="Марія Сидоренко", class_group=class5a)
# Students.objects.create(name="Андрій Лисенко", class_group=class6b)

# class5a = Class.objects.create(name="5-А")
# class6b = Class.objects.create(name="6-Б")

# students1 = Students.objects.create(name="Микола Лисенкович", class_group=class6b)
# students2 = Students.objects.create(name="Марія Федорівна", class_group=class6b)

# ukrainian = Subject.objects.create(name="Українська мова")
# it = Subject.objects.create(name="Інформатика")

# Grade.objects.create(student = students1,subject =ukrainian ,grade = 10,data=date(2025,9,1))
# Grade.objects.create(student = students1,subject =it ,grade = 7,data=date(2025,9,2))
# Grade.objects.create(student = students2,subject =ukrainian ,grade = 10,data=date(2025,9,1))
# Grade.objects.create(student = students2,subject =it ,grade = 6,data=date(2025,9,2))
                                                                  

# school_class = Class.objects.create(name="7-Б")
# pi = Subject.objects.create(name="Фізкульттура")
# teacher = Teacher.objects.create(name = "Ростік" ,surname = "Тюрін", subject = pi )

# Schedule.objects.create(
#     day_of_week= "Mon",
#     start_lessons = time(8,30),
#     end_lessons = time(9,15),
#     subject = pi,
#     school_class=school_class,
#     teacher=teacher
# )




