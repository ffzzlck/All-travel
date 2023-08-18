from modeltranslation.translator import translator, TranslationOptions
from .models import Title, Reason, ReasonTitle, FAQ, Question, Navbar


class TitleTranslationOption(TranslationOptions):
    fields = ('title', 'content')


class ReasonTranslationOption(TranslationOptions):
    fields = ('title', 'content')


class ReasonTitleTranslationOption(TranslationOptions):
    fields = ('title',)


class FAQTranslationOption(TranslationOptions):
    fields = ('title', 'content')


class QuestionTranslationOption(TranslationOptions):
    fields = ('title',)


class NavbarTranslationOption(TranslationOptions):
    fields = ('name',)


translator.register(Title, TitleTranslationOption)
translator.register(Reason, ReasonTranslationOption)
translator.register(ReasonTitle, ReasonTitleTranslationOption)
translator.register(FAQ, FAQTranslationOption)
translator.register(Question, QuestionTranslationOption)
translator.register(Navbar, NavbarTranslationOption)
