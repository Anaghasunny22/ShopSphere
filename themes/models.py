from django.db import models

# model for banner

class SiteSetting(models.Model):
    banner=models.ImageField(upload_to='media/site')
    caption=models.TextField()
