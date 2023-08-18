from django.contrib import admin
from .models import Contact, ContactUs


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'created_at', 'is_published')
    list_display_links = ('id', 'name', 'phone',)


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone', 'created_at',)
    list_display_links = ('id', 'phone',)


admin.site.register(Contact, ContactAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
