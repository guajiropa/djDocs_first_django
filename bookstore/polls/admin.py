"""
AUTHOR      :   Robert James Patterson
DATE:       :   10/02/2018
SYNOPSIS    :   Working thru the 'docs.djangoproject.com' tutorial
"""
from django.contrib import admin
from .models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)

