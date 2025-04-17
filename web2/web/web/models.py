# импортируем библиотеку дла создания модели БД средствами ORM
from django.db import models

class Person(models.Model):
    textbox1_text = models.CharField(max_length=200, null=False)
    textbox2_text = models.CharField(max_length=500, null=False)


