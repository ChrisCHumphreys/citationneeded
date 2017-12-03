from django.db import models


class Paper(models.Model):
    paper_name = models.CharField(max_length=60)
    file_link = models.FileField(upload_to="upload/")
