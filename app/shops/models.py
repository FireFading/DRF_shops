from django.db import models
from streets.models import Street


class Shop(models.Model):
    name = models.CharField(verbose_name="Название", max_length=128)
    street = models.ForeignKey(verbose_name="Улица", to=Street, on_delete=models.CASCADE, related_name="shops")
    opening_time = models.TimeField(verbose_name="Время открытия")
    closing_time = models.TimeField(verbose_name="Время закрытия")

    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"
        ordering = ["-name"]

    def __str__(self):
        return self.name
