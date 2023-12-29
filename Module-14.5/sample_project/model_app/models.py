from django.db import models

# Create your models here.
class PracticeModel(models.Model):
    pc_id=models.AutoField(primary_key=True)
    balance=models.BigIntegerField()
    binary_field=models.BinaryField()
    active=models.BooleanField()
    name=models.CharField(max_length=50)
    birth_day=models.DateField()
    appointment=models.DateTimeField()
    amount=models.DecimalField(max_digits=5,decimal_places=2)
    duration=models.DurationField()
    email=models.EmailField()
    age=models.IntegerField()
    slug=models.SlugField()
    comment=models.TextField()
    today=models.TimeField()
    img=models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name


