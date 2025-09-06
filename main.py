import django_setup
from model_system.models import Subject, Teacher, Class, Students

math = Subject.objects.create(name="Математика")
english = Subject.objects.create(name="Англійська мова")

teacher1 = Teacher.objects.create(name = "Ольга" ,surname = "Василівна", subject = math)
teacher2 = Teacher.objects.create(name = "Микола " ,surname = "Степанович", subject = english)

class5a = Class.objects.create(name="5-А")
class6b = Class.objects.create(name="6-Б")

Students.objects.create(name="Василь Коваль", class_group=class5a)
Students.objects.create(name="Марія Сидоренко", class_group=class5a)
Students.objects.create(name="Андрій Лисенко", class_group=class6b)

