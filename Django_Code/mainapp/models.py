from django.db import models

from django.db.models.fields import FloatField, BigIntegerField, CharField
# Create your models here.
        
class Member(models.Model):
    mem_id = CharField(primary_key=True, null=False, max_length=20)
    mem_pass = CharField(null=False,max_length=20)
    class Meta: 
        db_table="member"
        app_label="mainapp"
        managed=False