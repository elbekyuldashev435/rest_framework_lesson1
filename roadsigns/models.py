from django.db import models

# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=120)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return f"{self.name}"


class Documents(models.Model):
    category_name = models.ForeignKey(Categories, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='all/images', blank=True, null=True)
    video = models.FileField(upload_to='all/videos', blank=True, null=True)
    audio = models.FileField(upload_to='all/audios', blank=True, null=True)
    docs = models.FileField(upload_to='all/docs', blank=True, null=True)

    class Meta:
        db_table = 'documents'

    def __str__(self):
        return f"{self.name} {self.category_name.name}"