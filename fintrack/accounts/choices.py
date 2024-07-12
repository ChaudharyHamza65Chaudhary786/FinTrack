from django.db import models

class AccountCategoryChoices(models.TextChoices):
    current = "CURRENT", "Current"
    saving = "SAVING", "Saving"
