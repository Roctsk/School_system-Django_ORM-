import django_setup
from model_system.models import Subject, Teacher, Class, Students , Schedule ,Grade
from datetime import date , time


# math = Subject.objects.create(name="Математика")
# english = Subject.objects.create(name="Англійська мова")
# ukrainian = Subject.objects.create(name="Українська мова")
# it = Subject.objects.create(name="Інформатика")

# teacher1 = Teacher.objects.create(name="Ольга", surname="Василівна", subject=math)
# teacher2 = Teacher.objects.create(name="Микола", surname="Степанович", subject=english)
# teacher3 = Teacher.objects.create(name="Ірина", surname="Петрівна", subject=ukrainian)
# teacher4 = Teacher.objects.create(name="Ростік", surname="Тюрін", subject=it)


# class9a = Class.objects.create(name="9-А")
# class9b = Class.objects.create(name="9-Б")
# class10a = Class.objects.create(name="10-Б")
# class10b = Class.objects.create(name="10-A")
# class11a= Class.objects.create(name="11-A")
# class11b= Class.objects.create(name="11-Б")


# students1= Students.objects.create(name="Василь Коваль", class_group=class9a)
# students2= Students.objects.create(name="Марія Сидоренко", class_group=class9b)
# students3 = Students.objects.create(name="Андрій Лисенко", class_group=class10a)
# students4= Students.objects.create(name="Микола Лисенкович", class_group=class10b)
# students5 = Students.objects.create(name="Сегрій Федорук", class_group=class11a)
# students6 = Students.objects.create(name="Саша Тик", class_group=class11b)


# Grade.objects.create(student=students1, subject=english, grade=10, data=date(2025, 9, 1))
# Grade.objects.create(student=students2, subject=math, grade=7, data=date(2025, 9, 2))
# Grade.objects.create(student=students3, subject=ukrainian, grade=10, data=date(2025, 9, 1))
# Grade.objects.create(student=students4, subject=it, grade=6, data=date(2025, 9, 2))
# Grade.objects.create(student=students5, subject=english, grade=10, data=date(2025, 9, 1))
# Grade.objects.create(student=students6, subject=it, grade=7, data=date(2025, 9, 2))

# Schedule.objects.create(
#     day_of_week="Mon",
#     start_lessons=time(9, 00),
#     end_lessons=time(9, 45),
#     subject=math,
#     school_class=class9a,
#     teacher=teacher2
# )

# Schedule.objects.create(
#     day_of_week="Mon",
#     start_lessons=time(9, 00),
#     end_lessons=time(9, 45),
#     subject=math,
#     school_class=class9b,
#     teacher=teacher3
# )
# Schedule.objects.create(
#     day_of_week="Mon",
#     start_lessons=time(9, 00),
#     end_lessons=time(9, 45),
#     subject=math,
#     school_class=class10a,
#     teacher=teacher4
# )
# Schedule.objects.create(
#     day_of_week="Mon",
#     start_lessons=time(9, 00),
#     end_lessons=time(9, 45),
#     subject=math,
#     school_class=class10b,
#     teacher=teacher4
# )
# Schedule.objects.create(
#     day_of_week="Mon",
#     start_lessons=time(9, 00),
#     end_lessons=time(9, 45),
#     subject=math,
#     school_class=class11a,
#     teacher=teacher3
# )

# Schedule.objects.get_or_create(
#     day_of_week="Mon",
#     start_lessons=time(9, 00),
#     end_lessons=time(9, 45),
#     subject=math,
#     school_class=class11b,
#     teacher=teacher2
# )


def add_schedule():
    day = input("Введіть день (Mon/Tue/Web/Thu/Fri): ")
    start = input("Введіть час початку (год:хв): ")
    end = input("Введіть час завершення (год:хв): ")
    subject_name = input("Введіть предмет: ")
    class_name = input("Введіть клас: ")
    teacher_name = input("Введіть ім’я вчителя: ")

    try:
        subject = Subject.objects.get(name=subject_name)
        school_class = Class.objects.get(name=class_name)
        teacher = Teacher.objects.get(name=teacher_name, subject=subject)
    except Subject.DoesNotExist:
        print("Такого предмета немає!")
        return
    except Class.DoesNotExist:
        print(" Такого класу немає!")
        return
    except Teacher.DoesNotExist:
        print(" Такого вчителя немає!")
        return
    
    Schedule.objects.create(
        day_of_week = day,
        start_lessons = start,
        end_lessons = end,
        subject = subject,
        school_class = school_class,
        teacher = teacher
    )

    print("Заняття додано до розкладу1")

    
def add_grade():
    student_name = input("Введіть ПІБ учня: ")
    subject_name = input("Введіть предмет: ")
    grade = int(input("Введіть оцінку: "))
    grade_date = input("Введіть дату (YYYY-MM-DD): ")

    try:
        student = Students.objects.get(name=student_name)
        subject = Subject.objects.get(name=subject_name)
    except Students.DoesNotExist:
        print(" Учня не знайдено!")
        return
    except Subject.DoesNotExist:
        print("❌ Предмет не знайдено!")
        return
    
    Grade.objects.create(
        student=student,
        subject=subject,
        data = date.fromisoformat(grade_date),
        grade = grade
    )
    print("Оцінка успішно додано")

def main():
    while True:
        print("===Шкільна система===")
        print("1 - Додати заняття в розклад")
        print("2 - Додати оцінку")
        print(" 0 - Вийти")

        choice = input("Ваш вибір:")

        if choice == "1":
            add_schedule()
        elif choice == "2":
            add_grade()
        elif choice == "0":
            print("Вихід...")
            break
        else:
            print(" Невірний вибір!")



if __name__ == "__main__":
    main()