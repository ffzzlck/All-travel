from django.contrib import admin
from .models import About, Service


class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'is_published')
    list_display_links = ('title',)


class ContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'is_published')
    list_display_links = ('name',)


admin.site.register(About, AboutAdmin)
admin.site.register(Service, ContractAdmin)
