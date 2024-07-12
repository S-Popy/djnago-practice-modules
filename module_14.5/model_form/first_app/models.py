from django.db import models
import datetime
# Create your models here.

class ExampleModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    roll = models.IntegerField()
    mobile_number = models.BigIntegerField()
    binary_field = models.BinaryField()
    passed = models.BooleanField()
    date = models.DateTimeField(default=datetime.datetime.now)
    birth_date = models.DateField()
    class_length = models.DurationField()
    fees = models.DecimalField(max_digits=5, decimal_places=2)
    comments = models.TextField(blank = True)
