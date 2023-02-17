from django.db import models


# Create your models here.
class TODO(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="Заголовок", default="null")
    description = models.CharField(max_length=100, null=False, blank=False, verbose_name="Описание",
                                   default="null")
    detailed_description = models.TextField(max_length=2500, null=False, blank=False,
                                            verbose_name="Подробное описание", default="null")
    status = models.CharField(max_length=100, null=False, blank=False, default="new", verbose_name="Статус")
    completion_date = models.DateField(default="", verbose_name="Дата выполнения")

    def __str__(self):
        return f"{self.title} - {self.status}"
