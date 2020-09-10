from django.db import models
import datetime
# Create your models here.
class Task(models.Model):
    status = models.BooleanField()
    date = models.DateField()
    title = models.CharField(max_length=20)
    desc = models.TextField(blank=True)
    file = models.FileField(blank=True, upload_to='')

    def __str__(self):
        crr_date = self.date
        show = crr_date.strftime('%d %b %y')
        return f'{self.title} {show}'