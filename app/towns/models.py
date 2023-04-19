from django.db import models


class Town(models.Model):
    name = models.CharField(verbose_name="Название", max_length=128)

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"
        ordering = ["-name"]

    def __str__(self):
        return self.name
