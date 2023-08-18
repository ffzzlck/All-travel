from modeltranslation.translator import translator, TranslationOptions
from .models import About, Service


class AboutTranslationOption(TranslationOptions):
    fields = ('title', 'content')


class ServiceTranslationOption(TranslationOptions):
    fields = ('name', 'service', 'content')


translator.register(About, AboutTranslationOption)
translator.register(Service, ServiceTranslationOption)
