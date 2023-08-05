from django.db import models
from django.utils.translation import gettext_lazy as _


class Brand(models.Model):
    brdName = models.CharField(max_length=50)
    brdDescription = models.TextField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.brdName
    
    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")


# معقدة شوي هذي في الخدمة مبعد إن شاء الله نديروها
class Variant(models.Model):
    varName = models.CharField(max_length=50)
    varDescription = models.TextField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.varName
    
    class Meta:
        verbose_name = _("Variant")
        verbose_name_plural = _("Variants")

