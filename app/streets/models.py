from django.db import models
from towns.models import Town


class Street(models.Model):
    name = models.CharField(verbose_name="Название", max_length=128)
    town = models.ForeignKey(verbose_name="Город", to=Town, on_delete=models.CASCADE, related_name="shops")

    class Meta:
        verbose_name = "Улица"
        verbose_name_plural = "Улицы"
        ordering = ["-name"]

    def __str__(self):
        return self.name
