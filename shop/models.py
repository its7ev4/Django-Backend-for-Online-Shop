from django.db import models # type: ignore
from django.utils import timezone # type: ignore
# Create your models here.

# модель для категории
class Category(models.Model):
    title = models.CharField(max_length=255) #название
    created_at = models.DateTimeField(default=timezone.now) #дата (автоматическая)

    def __str__(self):
        return self.title

# модель для курса
class Course(models.Model):
    title = models.CharField(max_length=300)  #название
    price = models.FloatField()  #цена 
    students_qty = models.IntegerField() #кол-во студентов
    reviews_qty = models.IntegerField(default=0) #кол-во отзывов

    created_at = models.DateTimeField(default=timezone.now)
    #категория курса, связьо курса с категорией
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    #при удалении категории автоматический будут удалены все курса категории
    def __str__(self):
        return self.title

