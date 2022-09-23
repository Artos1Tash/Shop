from django.db import models


class SendEmail(models.Model):
    sender1 = models.EmailField('Type your emmail')
    text = models.CharField(max_length=128, null=True, blank=True)
