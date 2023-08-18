from django.db import models
from ckeditor.fields import RichTextField


class Title(models.Model):
    image = models.ImageField(upload_to='static/images')
    title = models.CharField(max_length=220)
    content = RichTextField()

    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class ReasonTitle(models.Model):
    title = models.CharField(max_length=220)

    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class ReasonImage(models.Model):
    image = models.ImageField(upload_to='static/images')

    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)


class Reason(models.Model):
    title = models.CharField(max_length=220)
    content = RichTextField()
    icon = models.ImageField(upload_to='static/images')

    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class FAQ(models.Model):
    icon = models.ImageField(upload_to='static/image')
    title = models.CharField(max_length=220)
    content = RichTextField()

    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Question(models.Model):
    image = models.ImageField(upload_to='static/images')
    title = models.CharField(max_length=220)

    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Navbar(models.Model):
    name = models.CharField(max_length=220)
    link = models.CharField(max_length=220)

    def __str__(self):
        return self.name
