from django.db import models
from django.utils.translation import gettext_lazy as _

class NewsTypes(models.TextChoices):
    INFO = 'info', _('Info')
    WARNUNG = 'warnung', _('Warnung')
    SUPPORT = 'support', _('Support')
    
class AppointmentCategory(models.TextChoices):
    PERSONAL = 'PERS', 'Persönlich'
    ORGANIZATION = 'ORG', 'Organisation'
    EXAM = 'EXM', 'Klausur'