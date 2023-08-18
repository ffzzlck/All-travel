from django.db import models
from ckeditor.fields import RichTextField


class About(models.Model):
    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'

    image = models.ImageField(upload_to='static/images')
    title = models.CharField(max_length=220)
    content = RichTextField()

    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Service(models.Model):
    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Service'

    image = models.ImageField(upload_to='static/images')
    name = models.CharField(max_length=220)
    service = models.CharField(max_length=220)
    content = RichTextField()

    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.name
