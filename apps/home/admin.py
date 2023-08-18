from django.contrib import admin
from .models import Title, Reason, FAQ, ReasonTitle, ReasonImage, Question, Navbar


class TitleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'is_published')
    list_display_links = ('id', 'title',)


class ReasonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'is_published')
    list_display_links = ('id', 'title',)


class FAQAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'is_published')
    list_display_links = ('id', 'title',)


class ReasonTitleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'is_published')
    list_display_links = ('id', 'title',)


class ReasonImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'is_published')


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at',)


class NavbarAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


admin.site.register(Title, TitleAdmin)
admin.site.register(Reason, ReasonAdmin)
admin.site.register(FAQ, FAQAdmin)
admin.site.register(ReasonTitle, ReasonTitleAdmin)
admin.site.register(ReasonImage, ReasonImageAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Navbar, NavbarAdmin)