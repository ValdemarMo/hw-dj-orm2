from django.db import models

# первичная база
# class Teacher(models.Model):
#     name = models.CharField(max_length=30, verbose_name='Имя')
#     subject = models.CharField(max_length=10, verbose_name='Предмет')
#
#     class Meta:
#         verbose_name = 'Учитель'
#         verbose_name_plural = 'Учителя'
#
#     def __str__(self):
#         return self.name
#
#
# class Student(models.Model):
#     name = models.CharField(max_length=30, verbose_name='Имя')
#     teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
#     group = models.CharField(max_length=10, verbose_name='Класс')
#
#     class Meta:
#         verbose_name = 'Ученик'
#         verbose_name_plural = 'Ученики'
#
#     def __str__(self):
#         return self.name
#

# модификация базы
class Teacher(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    subject = models.CharField(max_length=10, verbose_name='Предмет')

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    teacher = models.ManyToManyField(Teacher, related_name='students')
    group = models.CharField(max_length=10, verbose_name='Класс')

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'

    def __str__(self):
        return self.name
#
# class Mentor(models.Model):
#     teacher = models.ForeignKey(Teacher, related_name="mentors")
#     student = models.ForeignKey(Student, related_name="mentors")
# #
#
# class MembershipInline(admin.TabularInline):
#     model = Membership
#     extra = 1
# InlineModelAdminВ этом примере для модели используются значения по умолчанию Membership, а количество дополнительных форм добавления ограничено одной. Это можно настроить с помощью любых опций, доступных для InlineModelAdminклассов.
#
# Теперь создайте административные представления для моделей Personи Group:
#
# class PersonAdmin(admin.ModelAdmin):
#     inlines = [MembershipInline]
#
#
# class GroupAdmin(admin.ModelAdmin):
#     inlines = [MembershipInline]