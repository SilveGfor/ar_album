from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=150)  # имя
    image = models.ImageField(upload_to='')  # url картинки
    issue_year = models.CharField(max_length=150)  # год выпуска
    group = models.CharField(max_length=150)  # группа (11.5 = 5, 11.2 = 2)

    def __str__(self):
        return self.name
