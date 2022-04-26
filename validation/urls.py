from django.urls import re_path as url
from validation import views



urlpatterns=[
    url(r'^validationOF$',views.ValApi),
    url(r'^validationOF/([0-9]+)$',views.ValApi),
    
]