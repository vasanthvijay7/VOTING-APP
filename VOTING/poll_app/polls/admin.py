from django.contrib import admin
# registering models here
from .models import Question, choice

# Register your models here.
# to map each question to select. To add questions and choices for the question from the admin panel
admin.site.site_header = "Polls App Admin"
admin.site.site_title = "Polls App Admin Area"
admin.site.index_title = "Welcome to thr Polls App Admin Area"


class ChoiceInLine(admin.TabularInline):
    model = choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None,{'fields' : ['question_text']}),('Date Information', {
        'fields' : ['pub_date'], 'classes' : ['collapse']}), ]
    inlines = [ChoiceInLine]


admin.site.register(Question, QuestionAdmin)
