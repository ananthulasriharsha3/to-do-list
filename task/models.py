from django.db import models

# Create your models here.
class Details(models.Model):
    t_name=models.TextField(max_length=10)
    t_desc=models.TextField()
    t_date=models.DateField()

    def __str__(self):
        return self.t_name  
