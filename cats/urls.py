from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_cats, name='cats'),
    path('<cat_id>', views.cat_detail, name='cat_detail'),
]
