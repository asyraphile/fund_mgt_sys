from django.db import models
import uuid
# Create your models here.
"""
TASK 1: Data Model Design Create a Python class for representing an investment fund
"""
class Fund(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4, verbose_name="Fund ID")
    name = models.CharField(max_length=255, verbose_name="Fund Name")
    manager_name = models.CharField(max_length=255, verbose_name="Fund Manager Name")
    description = models.TextField(default="", verbose_name="Fund Description")
    nav = models.DecimalField(decimal_places=2, verbose_name="Fund Net Asset Value")
    performance = models.DecimalField(decimal_places=2, verbose_name="Fund Performance(%)")
    created_at = models.DateField(auto_now_add=True, editable=False, verbose_name="Fund Date of Creation")
    
