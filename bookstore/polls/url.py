"""
AUTHOR      :   Robert James Patterson
DATE:       :   10/02/2018
SYNOPSIS    :   Working thru the 'docs.djangoproject.com' tutorial
"""
from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),

    # example url = /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),

    # example url = /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),

    # example url  = /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote')

]

