from django.db import models

class category (models.Model):
    # Модель категорий
    name = models.CharField("Категория", max_length=100)
    descriptions= models.TextField("Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

# Create your models here.
