from .views import *
from django.urls import path

urlpatterns = [
    path('',  main, name='main'),
    path('about',  about, name='about' ),
    path('contacts',  contacts, name='contacts'),
    path('branches',  branches, name='branches'),
    path('branches/<int:branch_id>',  branches_detail, name='branches_detail'),
    path('branches/class/<int:branch_id>',  BranchDetailView.as_view(), name='branches_detail'),
    path('branch/add',  branch_add, name='branch_add'),
    path('feedback',  feedback, name='feedback'),
    path('addnews',  addnews, name='addnews'),

]

