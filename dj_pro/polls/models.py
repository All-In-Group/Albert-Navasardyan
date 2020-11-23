from django.db import models
#from django.forms import ModelForm
#from django.core.exceptions import NON_FIELD_ERRORS

# Create your models here.


class Task(models.Model):
    task_name = models.CharField(max_length=30)
    task_date= models.DateTimeField(null=True, blank=True)
    


# Create your models here.


    def __str__(self):
        return f"{self.id}"





