from django.db import models
from ckeditor.fields import RichTextField
from phone_field import PhoneField


class Contact(models.Model):
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ContactUs(models.Model):
    class Meta:
        verbose_name = 'ContactUs'
        verbose_name_plural = 'ContactUs'

    address = RichTextField()
    phone = models.CharField(max_length=200)
    email = models.EmailField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
