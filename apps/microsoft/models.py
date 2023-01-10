from django.db import models


class Apps(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    release_year = models.IntegerField()
    company_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
