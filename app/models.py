from django.db import models

class Catagory(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Series(models.Model):
    title = models.CharField(max_length=500)
    def __str__(self):
        return self.title
    

class Movie(models.Model):
    link = models.FilePathField(path='media', match=None, recursive=True, null=True, blank=True)

    title = models.CharField(max_length=500)
    thumbnail = models.CharField(max_length=500, null=True, blank=True)

    size = models.IntegerField(null=True, blank=True)
    duration = models.DecimalField(max_digits=5, decimal_places=2)

    uploaded_at = models.DateTimeField()
    tags = models.ManyToManyField(Catagory, blank=True)

    is_series = models.BooleanField(default=False, null=True, blank=True)
    series_name = models.ForeignKey(Series, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)
    