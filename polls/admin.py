from django.contrib import admin

# Register your models here.

from .models import Question,Choice

#admin.site.register(Question)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra=3

class QuestionAdmin(admin.ModelAdmin):
    #fields =["pub_date","question_text"]
    #customize the question section only
    list_display = ["question_text","pub_date"]
    list_filter=["pub_date"]
    search_fields=["question_text"]
    fieldsets=[
    ("Question Section",{"fields":["question_text"]}),
    ("Date Information",{"fields":["pub_date"],
                         "classes":["collapse"]},)
    ]
    inlines=[ChoiceInline]
    #list_display = ["question_text","pub_date"]
    
    
admin.site.register(Question,QuestionAdmin)
#admin.site.register(Choice)