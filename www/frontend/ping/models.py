from django.db import models
from django.forms import ModelForm

TASK_STATUS_CHOICES = (
        ('NEW', 'New'),
        ('CMPL', 'Completed'),
)

class PingJob(models.Model):
    host = models.CharField(max_length=255)
    result = models.TextField(default="")
    status = models.CharField(max_length=4, choices=TASK_STATUS_CHOICES,
            default='NEW')
    task_id = models.CharField(max_length=255)

    def get_absolute_url(self):
        return "/job/%s/" % self.id

class PingJobForm(ModelForm):

    class Meta:
        model = PingJob
        fields = ("host",)
